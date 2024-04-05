const Comment = ({ comment }) => {
    return (
        <div className="bg-gray-200 border border-gray-300 p-4 mb-4">
            <p>{comment.content}</p>
            <p>Commented by {comment.user}</p>
        </div>
    );
}

export default Comment;