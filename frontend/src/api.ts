import axios from 'axios';

var client = axios.create({
    timeout: 300000,
    baseURL: "http://localhost:8000"
});



const PREFIX = '/documents'

export const DocumentClient = {
    uploadDocuments: async (data: any) => {
        try {
            const response = await client.post(PREFIX + '/upload', data, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            console.log("Response", response);

        } catch (error) {
            console.log("Error uploading files", error);
        }
    },
    ask: async (question: string) => {
        try {
            const response = await client.post(PREFIX + '/ask', { question });

            return response.data;

        } catch (error) {
            console.log("Can't answer questions", error)
            return []
        }
    }
}