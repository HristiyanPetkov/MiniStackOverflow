import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import Comment from "./Comment";

const question = {
    id: 3,
    title: "Direct register manipulation on Arduino Uno R4",
    description: "I want to generate a PWM signal on pin 9 (P303) using direct register manipulation." +
        " The new chip used on the Arduino Uno R4 is from Renesas and I found the documentation for the it." +
        " The problem is that I think that the Arduino IDE does not have support for this microcontroller" +
        " registers like they do for the Atmega328 chips. For example, I tried to call the register GPT321. " +
        "GTPR but the IDE does not recognize it. How should I solve this problem?",
    user: "Margin Petrisor-Victor",
}

const comments = [
    {
        id: 1,
        content: "You should use the new Arduino IDE 2.0",
        user: "John",
    },
    {
        id: 2,
        content: "I think that you should use the new Arduino IDE 2.0",
        user: "John",
    },
];

const QuestionPage = () => {
    //const [question, setQuestion] = useState({});
    const id = useParams().questionId;

    // useEffect(() => {
    //     const fetchQuestion = async () => {
    //         const response = await fetch(`http://localhost:8000/questions/${id}`);
    //         const data = await response.json();
    //         setQuestion(data);
    //     };
    //     fetchQuestion().then(r => console.log(r));
    // }, []);

    return (
        <div className="bg-gray-100 border border-gray-300 p-4 mb-4 w-7/12 mx-auto">
            <div>
                <h1 className="text-2xl font-bold mb-2">{question.title} </h1>
                <p className="text-gray-800 text-xs">{question.description}</p>
                <p className="text-gray-800 text-xs">Asked by {question.user}</p>

            </div>
            <div>
                <h2 className="text-2xl font-bold mb-2">Comments</h2>
                <ul>
                    {comments.map((comment) => (
                        <li key={comment.id}>
                            <Comment comment={comment} />
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default QuestionPage;