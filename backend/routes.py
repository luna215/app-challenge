import os
import logging


from pydantic import BaseModel
from typing import List
from fastapi import (
    APIRouter,
    HTTPException,
    File,
    UploadFile,
    status
)

from utils import *


router = APIRouter(dependencies=[])


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_documents(files: List[UploadFile] = File(...)):
    """Save PDF embeddings to database"""

    try:
        for file in files:
            file_path = os.path.join("/tmp", file.filename)

            # save file locally
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())

            text = extract_text_from_pdf(file_path)

            processed_text = preprocess_text(text)
            embeddings = generate_embeddings(processed_text)

            store_embeddings(embeddings, text)

        return "successful"
    except Exception as e:
        logging.error("Something went wrong", e)
        raise HTTPException(status_code=500, detail="Something went wrong on the server.")



class QuestionRequest(BaseModel):
    question: str


@router.post("/ask", status_code=status.HTTP_200_OK)
async def answer_question(question_request: QuestionRequest):
    """Answer user's question"""

    try:
        logging.info(f"Answering: {question_request.question}")
        question = question_request.question
        question_embedding = get_question_embedding(question)
        document_embeddings = get_document_embeddings()
        similarities = compute_similarity(question_embedding, document_embeddings)
        answers = generate_answers(similarities)

        # TOOD: Parse text to be more human readable
        return answers
    
    except Exception as e:
        logging.error("Something went wrong", e)
        raise HTTPException(status_code=500, detail="Something went wrong on the server.")

    return answers
    