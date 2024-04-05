import React from 'react';

const Comment = ({ comment }) => {
    const keywords = ["const", "let", "var", "if", "else", "for", "while", "function"];

    const highlightKeywords = (line) => {
        return line.split(/\b/).map((word, index) => {
            if (keywords.includes(word)) {
                return <span key={index} className="text-blue-500">{word}</span>;
            }
            return word;
        });
    };


    const contentLines = comment.content.split('\n');

    return (
        <div className="bg-gray-200 border border-gray-300 p-4 mb-4">
            {contentLines.map((line, index) => (
                <p key={index} className={line.startsWith('    ') ? 'bg-gray-800 text-gray-200 p-2 whitespace-pre-wrap' : ''}>
                    {highlightKeywords(line)}
                </p>
            ))}
            <p>Commented by {comment.user}</p>
        </div>
    );
}

export default Comment;
