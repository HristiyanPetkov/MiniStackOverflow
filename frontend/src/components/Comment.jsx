const Comment = ({ comment }) => {
    return (
        <div className="text-xs border-b border-gray-300 p-2">
            <p>{comment.content} - {comment.user}</p>
        </div>
    );
}

export default Comment;