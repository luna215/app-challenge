import {
  Button
} from "@chakra-ui/react";


import { DocumentClient } from '../api';
import { useState } from 'react';


interface AddDocumentProps {}

// Define a custom interface that extends HTMLInputAttributes
interface DirectoryInputAttributes extends React.InputHTMLAttributes<HTMLInputElement> {
    webkitdirectory?: boolean;
}
  

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
            <input 
                type="file" 
                // @ts-ignore
                webkitdirectory
                multiple 
                onChange={(e) => setFiles(e.target.files)} 
                
                />
            <Button
                mt={4} 
                colorScheme="purple" 
                onClick={handleFileUpload}>
            Upload
            </Button>
        </div>
    );
}