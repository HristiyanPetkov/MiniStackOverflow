import React from 'react';
import Question from './Question';

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
    }
];

const HomePage = () => {
    return (
        <div>
            <h1 className="text-center" >HomePage</h1>
            <ul className="flex-col flex">
                <p>Amount: {questions.length}</p>
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