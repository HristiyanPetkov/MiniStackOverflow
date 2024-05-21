from questions.models import Question
from extensions import db
import redis

# Create a connection to the Redis server with database name cache-LVFMKUIY
host = 'redis-19916.c250.eu-central-1-1.ec2.redns.redis-cloud.com'
port = 19916
password = "cWjOTj69Lk2mGiMs9O9aKI2SRJ5lnubm"

# Connect to the Redis server
r = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

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

    question_key = f"question_{new_question.id}"
    r.set(question_key, new_question.author_id)

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

def delete_question_by_id(question_id):
    question = Question.query.get(question_id)

    db.session.delete(question)
    db.session.commit()

    message = {
        "message": "Question deleted"
    }

    return message

def delete_all_questions():
    questions = Question.query.all()

    for question in questions:
        db.session.delete(question)
        db.session.commit()

    message = {
        "message": "All questions deleted"
    }

    return message
