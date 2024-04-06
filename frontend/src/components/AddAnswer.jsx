import Answer from "./Answer";
import React, {useState} from "react";
import TextWithPreview from "./TextWithPreview";

const AddAnswer = ({onAddAnswer}) => {
    const [answer, setAnswer] = useState('');
    console.log(onAddAnswer);

    return (
        <div className="flex flex-col">
            <TextWithPreview text={answer} setText={setAnswer} />
            <button onClick={() => onAddAnswer(answer)} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl mt-2 mx-auto mb-4 w-1/4">
                Submit
            </button>
        </div>
    );
}

export default AddAnswer;