import {
  Button
} from "@chakra-ui/react";


import { DocumentClient } from '../api';
import { useState } from 'react';


interface AddDocumentProps {}


export const AddDocument: React.FC<AddDocumentProps> = () => {
    const [files, setFiles] = useState<FileList | null>(null);

    const handleFileUpload = async () => {
        if (!files) return;

        const formData = new FormData();

        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }

        console.log("Form Data", formData);
        DocumentClient.uploadDocuments(formData);
    }

    return (
        <div>
            <input type="file" multiple onChange={(e) => setFiles(e.target.files)} />
            <Button
                mt={4} 
                colorScheme="purple" 
                onClick={handleFileUpload}>
            Upload
            </Button>
        </div>
    );
}