import React, {useState} from "react";
import axios from "axios";
import {useNavigate} from "react-router-dom";
import TextWithPreview from "./TextWithPreview";

const AskQuestion = () => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const navigator = useNavigate();

    // const keywords = ["const", "let", "var", "if", "else", "for", "while", "function"];
    // const contentLines = description.split('\n');
    //
    // const highlightKeywords = (line) => {
    //     return line.split(/\b/).map((word, index) => {
    //         if (keywords.includes(word)) {
    //             return <span key={index} className="text-blue-500">{word}</span>;
    //         }
    //         return word;
    //     });
    // };
    // const handleInputChange = (e) => {
    //     setDescription(e.target.value);
    // }

    const handleSubmit = (e) => {
        // const response = axios.post('http://localhost:8000/api/questions', {
        //     title: title,
        //     description: description,
        // });
        //
        // console.log(response);


        console.log('Title:', title);
        console.log('Description:', description);

        navigator('/');
    };

    return (
        <div className="container mx-auto">
            <h1 className="text-4xl text-center">Ask a question</h1>
            <div className="flex justify-center">
                <form className="w-3/4">
                    <div className="mb-4">
                        <label className="block mb-2 text-xl">Title:</label>
                        <input
                            type="text"
                            value={title}
                            className="w-full px-3 py-2 border rounded"
                        />
                    </div>
                    <div className="mb-4">
                        <div className="flex justify-between text-xl">
                            <label className="block mb-2">Description:</label>
                            <label className="black mb-2 w-1/2">Preview:</label>
                        </div>
                        <div>
                            <TextWithPreview text={description} setText={setDescription} />
                        </div>
                    </div>
                    <button
                        type="submit"
                        className="bg-blue-600 text-white px-4 py-2 rounded-xl mt-4 hover:bg-blue-500 mx-auto"
                        onClick={handleSubmit}
                    >
                        Submit
                    </button>
                </form>
            </div>
        </div>
    );
}

export default AskQuestion;