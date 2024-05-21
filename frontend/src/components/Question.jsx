// Question.js
import React from 'react';
import {Link} from "react-router-dom";

const Question = ({ question }) => {
    const truncatedContent = question.description.length > 200 ?
        question.description.slice(0, 200).split(' ').slice(0, -1).join(' ') + '...'
        : question.description;

    return (
        <div className="bg-gray-100 border border-gray-300 p-4 mb-4 w-7/12 mx-auto shadow-md rounded-3xl">
            <Link to={`/questions/${question.id}`} className="text-2xl font-bold mb-2">{question.title} </Link>
            <p className="text-gray-800 text-xs">{truncatedContent}</p>
            <p className="text-gray-800 text-xs">Asked by {question.user}</p>
        </div>
    );
};

export default Question;
