import React, {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import Answer from "./Answer";
import AddAnswer from "./AddAnswer";
import TextFormatter from "./TextFormatter";

const question = {
    id: 3,
    title: "Direct register manipulation on Arduino Uno R4",
    description: " I want to generate a PWM signal on pin 9 (P303) using direct register manipulation.\n" +
        " The new chip used on the Arduino Uno R4 is from Renesas and I found the documentation for the it." +
        " The problem is that I think that the Arduino IDE does not have support for this microcontroller" +
        " registers like they do for the Atmega328 chips. For example, I tried to call the register GPT321. " +
        "GTPR but the IDE does not recognize it. How should I solve this problem?\n" +
        "    const a = 0;\n" +
        "    const b = 1;\n" +
        "    const c = a + b;\n",
    user: "Margin Petrisor-Victor",
}

const answers = [
    {
        id: 1,
        content: "You should use the new Arduino IDE 2.0",
        user: "John",
        comments: [],
    },
    {
        id: 2,
        content: "I think that you should use the new Arduino IDE 2.0",
        user: "John",
        comments: [
            {
                id: 1,
                content: "I think that",
                user: "John",
            }
        ],
    },
    {
        id: 3,
        content: "I think that you should use the new Arduino IDE 2.0\n" +
            "    const a = 0;\n" +
            "    const b = 1;\n" +
            "    const c = a + b;\n",
        user: "John",
        comments: [],
    }
];

const QuestionPage = () => {
    //const [question, setQuestion] = useState({});
    //const [comments, setComments] = useState([]);
    const id = useParams().questionId;
    const [buttonClicked, setButtonClicked] = useState(false);

    // useEffect(() => {
    //     const fetchQuestion = async () => {
    //         const response = await fetch(`http://localhost:8000/questions/${id}`);
    //         const data = await response.json();
    //         setQuestion(data);
    //     };
    //     fetchQuestion().then(r => console.log(r));
    // }, []);

    const changeButtonState = () => {
        setButtonClicked(!buttonClicked);
    }

    const handleAddAnswer = async (answer) => {
        console.log('Add Answer');
        setButtonClicked(!buttonClicked);
        answers.push({
            id: answers.length + 1,
            content: answer,
            user: 'John',
            comments: [],
        });
    }

    return (
        <div className="bg-gray-100 border border-gray-300 p-4 mb-4 w-7/12 mx-auto rounded-3xl">
            <div>
                <h1 className="text-3xl font-bold mb-2">{question.title} </h1>
                <TextFormatter text={question.description} />
                <br/>
                <p className="text-gray-800">Asked by {question.user}</p>
            </div>
            <div>
                <div className="flex justify-between pb-2">
                    <h2 className="text-2xl font-bold mb-2 mt-2">Answers {answers.length}</h2>
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl " onClick={changeButtonState}>Add Answer</button>
                </div>
                {buttonClicked && (
                    <AddAnswer
                        onAddAnswer={handleAddAnswer}
                    />
                )}

                <ul>
                    {answers.map((answer) => (
                        <li key={answer.id}>
                            <Answer answer={answer} />
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default QuestionPage;