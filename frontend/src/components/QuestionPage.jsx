import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import Answer from "./Answer";

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
    {
        id: 3,
        content: "I think that you should use the new Arduino IDE 2.0\n" +
            "    const a = 0;\n" +
            "    const b = 1;\n" +
            "    const c = a + b;\n",
        user: "John",
    }
];

const QuestionPage = () => {
    //const [question, setQuestion] = useState({});
    //const [comments, setComments] = useState([]);
    const id = useParams().questionId;
    const [buttonClicked, setButtonClicked] = useState(false);

    const [comment, setComment] = useState('');

    const handleSubmit = () => {
        console.log('Submitted comment:', comment);
        comments.push({
            id: comments.length + 1,
            content: comment,
            user: 'John',
        });

        setComment('');
    };

    const handleInputChange = (event) => {
        setComment(event.target.value);
    };

    // useEffect(() => {
    //     const fetchQuestion = async () => {
    //         const response = await fetch(`http://localhost:8000/questions/${id}`);
    //         const data = await response.json();
    //         setQuestion(data);
    //     };
    //     fetchQuestion().then(r => console.log(r));
    // }, []);

    const AddComment = () => {
        console.log('Add Answer');
        setButtonClicked(!buttonClicked);
    }

    return (
        <div className="bg-gray-100 border border-gray-300 p-4 mb-4 w-7/12 mx-auto">
            <div>
                <h1 className="text-3xl font-bold mb-2">{question.title} </h1>
                <p className="text-gray-800">{question.description}</p>
                <br/>
                <p className="text-gray-800">Asked by {question.user}</p>
            </div>
            <div>
                <div className="flex justify-between pb-2">
                    <h2 className="text-2xl font-bold mb-2 mt-2">Comments</h2>
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded " onClick={AddComment}>Add Comment</button>
                </div>
                {buttonClicked && (
                    <div className="flex flex-col">
                        <div className="flex">
                            <textarea
                                value={comment}
                                onChange={handleInputChange}
                                placeholder="Enter your comment"
                                className="border border-gray-300 p-2 mb-2 w-1/2"
                            />
                            <div className="ml-2 w-1/2">
                                <h3 className="text-lg font-bold mb-2">Preview:</h3>
                                {comment.length > 0 && (
                                    <Answer comment={{ content: comment, user: 'John' }} />
                                )}
                            </div>

                        </div>
                        <button onClick={handleSubmit} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-2 mx-auto mb-4 w-1/4">
                            Submit
                        </button>
                    </div>
                )}

                <ul>
                    {comments.map((comment) => (
                        <li key={comment.id}>
                            <Answer comment={comment} />
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default QuestionPage;