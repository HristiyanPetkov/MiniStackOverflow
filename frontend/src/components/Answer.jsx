import React, { useState } from 'react';
import Comment from './Comment';

const Answer = ({ answer }) => {
    const keywords = ["const", "let", "var", "if", "else", "for", "while", "function"];
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

    const highlightKeywords = (line) => {
        return line.split(/\b/).map((word, index) => {
            if (keywords.includes(word)) {
                return <span key={index} className="text-blue-500">{word}</span>;
            }
            return word;
        });
    };

    const contentLines = answer.content.split('\n');

    return (
        <div className="bg-gray-200 border border-gray-300 p-4 mb-4 rounded-3xl">
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
