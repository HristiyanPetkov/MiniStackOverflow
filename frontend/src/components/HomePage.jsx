import React, {useEffect, useState} from 'react';
import Question from './Question';
import {Link} from "react-router-dom";

const questions = [
    {
        id: 1,
        title: "What is the capital of France?",
        description: "I am trying to learn the capitals of the world",
        user: "John",
    },
    {
        id: 2,
        title: "What is the capital of Germany?",
        description: "I am trying to learn the capitals of the world",
        user: "John",
    },
    {
        id: 3,
        title: "Direct register manipulation on Arduino Uno R4",
        description: "I want to generate a PWM signal on pin 9 (P303) using direct register manipulation." +
            " The new chip used on the Arduino Uno R4 is from Renesas and I found the documentation for the it." +
            " The problem is that I think that the Arduino IDE does not have support for this microcontroller" +
            " registers like they do for the Atmega328 chips. For example, I tried to call the register GPT321. " +
            "GTPR but the IDE does not recognize it. How should I solve this problem?",
        user: "Margin Petrisor-Victor",
    },
    {
        id: 5,
        title: "How to use the new React Context API?",
        description: "I am trying",
        user: "John",
    },
    {
        id: 6,
        title: "How to use the new React Context API?",
        description: "I am trying",
        user: "John",
    },
    {
        id: 7,
        title: "How to use the new React Context API?",
        description: "I am trying",
        user: "John",
    }
];

const HomePage = () => {
    // const [questions, setQuestions] = useState([]);
    //
    // useEffect(() => {
    //     const fetchQuestions = async () => {
    //         const response = await fetch('http://localhost:8000/questions');
    //         const data = await response.json();
    //         setQuestions(data);
    //     };
    //     fetchQuestions().then(r => console.log(r));
    // }, []);

    return (
        <div>
            <h1 className="text-center text-4xl" >Questions</h1>
            <ul>
                <div className="flex justify-between mx-auto w-7/12 mb-2 items-center">
                    <p className="text-2xl">Amount: {questions.length}</p>
                    <Link to={'/askQuestion'}>
                        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl ">Ask Question</button>
                    </Link>
                </div>

                {questions.map((question) => (
                    <li key={question.id}>
                        <Question question={question} />
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default HomePage;