from questions.models import Question
from extensions import db

def create_question(data):
    new_question = Question(
        title=data['title'],
        body=data['body'],
        user_id=data['user_id']
    )
    
    db.session.add(new_question)
    db.session.commit()

    return new_question, None

def get_question_by_id(question_id):
    question = Question.query.get(question_id)

    return question, None

def resolve_question_by_id(question_id):
    question = Question.query.get(question_id)
    question.is_resolved = True

    db.session.commit()

    return question, None
