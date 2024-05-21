import React from "react";

const TextFormatter = ({ text }) => {
    const keywords = ["const", "let", "var", "if", "else", "for", "while", "function"];
    const contentLines = text.split('\n');

    const highlightKeywords = (line) => {
        return line.split(/\b/).map((word, index) => {
            if (keywords.includes(word)) {
                return <span key={index} className="text-blue-500">{word}</span>;
            }
            return word;
        });
    };

    return (
        <div>
            {contentLines.map((line, index) => {
                if (line.startsWith('    ') && line.length > 4) {
                    return (
                        <p key={index} className="bg-gray-800 text-gray-200 whitespace-pre-wrap">
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
        </div>
    );
}

export default TextFormatter;