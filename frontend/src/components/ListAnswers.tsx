import { useState } from 'react';

import {
    Button,
    Input,
    Heading,
    UnorderedList,
    ListItem
} from "@chakra-ui/react";
import { DocumentClient } from '../api';

interface LstDocumentsProps {}

export const ListAnswers: React.FC<LstDocumentsProps> = ({}) => {
    const [question, setQuestion] = useState<any>("");
    const [answers, setAnswers] = useState<any>([]);


    const getAnswer = async () => {
        console.log("User asking", question);
        const listAnswers = await DocumentClient.ask(question);
        setAnswers(listAnswers);
    }


    return (
        <div>
            <Heading as='h2' size='2xl'>Ask a question</Heading>
            <Input placeholder="Ask question" onChange={(e) => setQuestion(e.target.value)}/>
            <Button onClick={getAnswer}>Get answer</Button>
            <UnorderedList>
                { answers.map( (item: any) => (<ListItem>{item}</ListItem>))}
            </UnorderedList>
        </div>
    )
}
