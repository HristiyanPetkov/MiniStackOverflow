import React, {useState} from "react";
import TextFormatter from "./TextFormatter";

const TextWithPreview = ({ text, setText }) => {
    const handleInputChange = (e) => {
        setText(e.target.value);
    }

    return (
        <div className="flex">
            <textarea
                value={text}
                onChange={handleInputChange}
                placeholder="Enter your answer"
                className="border border-gray-300 p-2 mb-2 mr-4 w-1/2"
            />
            <div className="preview-container w-1/2">
                <TextFormatter text={text} setText={setText} />
            </div>
        </div>
    );
}

export default TextWithPreview;