from comments.models import Comment
from extensions import db
from datetime import datetime

def create_comment_object(data):
    helper = datetime.now()
    helper = helper.strftime("%Y-%m-%d %H:%M:%S")
    
    new_comment = Comment(
        answer_id = data['answer_id'],
        user_id = data['user_id'],
        publication_ts = helper,
        body = data['body']
    )
    
    db.session.add(new_comment)
    db.session.commit()

    new_question = Comment.query.order_by(Comment.id.desc()).first()

    message = {
        "id": new_comment.id,
        "answer_id": new_comment.answer_id,
        "user_id": new_comment.user_id,
        "publication_ts": new_comment.publication_ts,
        "body": new_comment.body
    }

    return message


def get_comments_by_answer_id(answer_id):
    # TODO check; if not get => all
    comments = Comment.query.get(answer_id)

    message = {}
    index = 0
    for comment in comments:
        message[index] = {
            "id": comment.id,
            "answer_id": comment.answer_id,
            "user_id": comment.user_id,
            "publication_ts": comment.publication_ts,
            "body": comment.body
        }
        index += 1

    return message


def delete_comment_by_id(comment_id):
    comment = Comment.query.get(comment_id)

    db.session.delete(comment)
    db.session.commit()

    message = {
        "message": "Comment deleted"
    }

    return message


def delete_all_comments():
    comments = Comment.query.all()

    for comment in comments:
        db.session.delete(comment)
        db.session.commit()

    message = {
        "message": "All comments deleted"
    }

    return message