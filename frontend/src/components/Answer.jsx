import React, { useState } from 'react';
import Comment from './Comment';
import TextFormatter from "./TextFormatter";

const Answer = ({ answer }) => {
    const [newComment, setNewComment] = useState('');

    const handleCommentChange = (e) => {
        setNewComment(e.target.value);
    };

    const handleSubmitComment = () => {
        console.log('New comment:', newComment);
        answer.comments.push({
            id: answer.comments.length + 1,
            content: newComment,
            user: 'John',
        });

        setNewComment('');
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleSubmitComment();
        }
    };

    return (
        <div className="bg-gray-200 border border-gray-300 p-4 mb-4 rounded-3xl">
            <TextFormatter text={answer.content} />
            <br/>
            <p className="mb-3">Commented by {answer.user}</p>
            <div className="border-b border-black" />
            {answer.comments.map((comment) => (
                <li key={comment.id}>
                    <Comment comment={comment} />
                </li>
            ))}
            <input
                type="text"
                value={newComment}
                onChange={handleCommentChange}
                onKeyUp={handleKeyPress}
                placeholder="Add a comment..."
                className="bg-gray-200 mt-2 p-1 w-full"
            />
        </div>
    );
}

export default Answer;
