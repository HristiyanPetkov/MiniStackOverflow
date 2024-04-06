import React, {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import Answer from "./Answer";

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

    const [answer, setAnswer] = useState('');

    const keywords = ["const", "let", "var", "if", "else", "for", "while", "function"];
    const contentLines = question.description.split('\n');
    console.log(contentLines);

    const highlightKeywords = (line) => {
        return line.split(/\b/).map((word, index) => {
            if (keywords.includes(word)) {
                return <span key={index} className="text-blue-500">{word}</span>;
            }
            return word;
        });
    };

    const handleSubmit = () => {
        console.log('Submitted answer:', answer);
        answers.push({
            id: answers.length + 1,
            content: answer,
            user: 'John',
        });

        setAnswer('');
    };

    const handleInputChange = (event) => {
        setAnswer(event.target.value);
    };

    // useEffect(() => {
    //     const fetchQuestion = async () => {
    //         const response = await fetch(`http://localhost:8000/questions/${id}`);
    //         const data = await response.json();
    //         setQuestion(data);
    //     };
    //     fetchQuestion().then(r => console.log(r));
    // }, []);

    const AddAnswer = () => {
        console.log('Add Answer');
        setButtonClicked(!buttonClicked);
    }

    return (
        <div className="bg-gray-100 border border-gray-300 p-4 mb-4 w-7/12 mx-auto rounded-3xl">
            <div>
                <h1 className="text-3xl font-bold mb-2">{question.title} </h1>
                {contentLines.map((line, index) => {
                    if (line.startsWith('    ')) {
                        return (
                            <p key={index} className="bg-gray-800 text-gray-200 p-2 whitespace-pre-wrap">
                                {highlightKeywords(line)}
                            </p>
                        );
                    } else {
                        return (
                            <p key={index}>
                                {line}
                            </p>
                        );
                    }
                })}
                <br/>
                <p className="text-gray-800">Asked by {question.user}</p>
            </div>
            <div>
                <div className="flex justify-between pb-2">
                    <h2 className="text-2xl font-bold mb-2 mt-2">Answers {answers.length}</h2>
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl " onClick={AddAnswer}>Add Answer</button>
                </div>
                {buttonClicked && (
                    <div className="flex flex-col">
                        <div className="flex">
                            <textarea
                                value={answer}
                                onChange={handleInputChange}
                                placeholder="Enter your answer"
                                className="border border-gray-300 p-2 mb-2 w-1/2"
                            />
                            <div className="ml-2 w-1/2">
                                <h3 className="text-lg font-bold mb-2">Preview:</h3>
                                {answer.length > 0 && (
                                    <Answer answer={{ content: answer, user: 'John' }} />
                                )}
                            </div>

                        </div>
                        <button onClick={handleSubmit} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl mt-2 mx-auto mb-4 w-1/4">
                            Submit
                        </button>
                    </div>
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