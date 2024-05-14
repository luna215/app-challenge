import re
import pytesseract
import torch
import uuid
import numpy as np

from pymongo import MongoClient
from transformers import BertTokenizer, BertModel
from pdf2image import convert_from_path


# Connect to MongoDB server
client = MongoClient('mongodb://mongodb:27017/')
db = client['embedding_database']  # Choose or create a database
collection = db['embeddings']  # Choose or create a collection

# Initialize BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def store_embeddings(embeddings, text):
    """Store embeddings to database"""
    
    for embedding in embeddings:
        document = {
            "embedding_id": f'{uuid.uuid4()}',
            "text": text,
            "embedding_vector": embedding.tolist()}
        collection.insert_one(document)


def generate_embeddings(text: str):
    """Generate embeddings using BERT model""" 
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy() # Average pooling over tokens

    return embeddings        


def preprocess_text(text: str):
    """Process text to tokenize, remove special characters"""

    # Remove special character
    no_special_characters = re.sub(r'[^\w\s]', '', text)

    
    # Tokenize
    tokens = tokenizer.tokenize(no_special_characters)

    return tokens


def extract_text_from_pdf(pdf_path: str):
    """Run OCR on scanned PDFs"""
    text = ""
    pages = convert_from_path(pdf_path)
    for page in pages:
        text += pytesseract.image_to_string(page)
    
    return text


def get_question_embedding(question: str):
    """Retrieve question"""

    inputs = tokenizer(question, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        question_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    
    return question_embedding


def get_document_embeddings():
    """Get document embeddings from MongoDB"""

    embeddings = []
    for document in collection.find():
        embeddings.append(document['embedding_vector'])
    
    return embeddings


def compute_similarity(question_embedding, document_embeddings):
    """Compute similarity between question and document embeddings"""

    similarities = []
    for document_embedding in document_embeddings:
        similarity = np.dot(question_embedding, document_embedding) / (np.linalg.norm(question_embedding) * np.linalg.norm(document_embedding))
        similarities.append(similarity)
    
    return similarities


def generate_answers(similarities):
    """Generate answers based on document embeddings"""

    # Example: return the document with the highest similarity as the answer
    similarities_list = np.array(list(similarities))
    top_ten_indices = np.argpartition(-similarities_list, 10)[:10]

    documents = list(collection.find())
    answers = set()

    for similar_idx in top_ten_indices:
        answers.add(documents[similar_idx]['text'])

    return answers