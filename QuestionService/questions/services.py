from questions.models import Question
from extensions import db

def create_question_object(data):
    new_question = Question(
        title=data['title'],
        body=data['body'],
        author_id=data['author_id']
    )
    
    db.session.add(new_question)
    db.session.commit()

    new_question = Question.query.order_by(Question.id.desc()).first()

    message = {
        "id": new_question.id,
        "title": new_question.title,
        "body": new_question.body,
        "is_resolved": new_question.is_resolved,
        "author_id": new_question.author_id
    }

    return message

def get_question_by_id(question_id):
    question = Question.query.get(question_id)

    message = {
        "id": question.id,
        "title": question.title,
        "body": question.body,
        "is_resolved": question.is_resolved,
        "author_id": question.author_id
    }

    return message

def get_all_questions():
    questions = Question.query.all()

    message = {}

    for question in questions:
        message[question.id] = {
            "id": question.id,
            "title": question.title,
            "body": question.body,
            "is_resolved": question.is_resolved,
            "author_id": question.author_id
        }

    return message

def resolve_question_by_id(question_id):
    question = Question.query.get(question_id)
    question.is_resolved = True

    db.session.commit()

    message = {
        "id": question.id,
        "title": question.title,
        "body": question.body,
        "is_resolved": question.is_resolved,
        "author_id": question.author_id
    }

    return message

def is_resolved_by_id(question_id):
    question = Question.query.get(question_id)

    message = {
        "is_resolved": question.is_resolved
    }

    return message
