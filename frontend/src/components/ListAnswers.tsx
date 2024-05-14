import { useState } from 'react';

import {
    Button,
    Input,
    Heading
} from "@chakra-ui/react";
import { DocumentClient } from '../api';

interface LstDocumentsProps {}

export const ListAnswers: React.FC<LstDocumentsProps> = ({}) => {
    const [question, setQuestion] = useState<any>([]);


    const getAnswer = async () => {
        console.log("User asking", question);
        await DocumentClient.ask(question);
    }


    return (
        <div>
            <Heading as='h2' size='2xl'>Ask a question</Heading>
            <Input placeholder="Ask question" onChange={(e) => setQuestion(e.target.value)}/>
            <Button onClick={getAnswer}>Get answer</Button>
        </div>
    )
}
