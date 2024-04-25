from answers.models import Answer
from extensions import db
import requests
import redis

# Create a connection to the Redis server with database name cache-LVFMKUIY
host = 'redis-19916.c250.eu-central-1-1.ec2.redns.redis-cloud.com'
port = 19916
password = "cWjOTj69Lk2mGiMs9O9aKI2SRJ5lnubm"

# Connect to the Redis server
r = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

def create_answer_object(data):
    is_resolved_response = requests.get(f"http://localhost:8000/questions/is_resolved/{data['question_id']}")
    is_resolved = is_resolved_response.json()['is_resolved']

    if is_resolved:
        message = {
            "error": "Question is already resolved"
        }
    else:
        new_answer = Answer(
            body=data['body'],
            question_id=data['question_id'],
            author_id=data['author_id']
        )
        
        db.session.add(new_answer)
        db.session.commit()

        new_answer = Answer.query.order_by(Answer.id.desc()).first()

        message = {
            "id": new_answer.id,
            "body": new_answer.body,
            "is_final": new_answer.is_final,
            "question_id": new_answer.question_id,
            "author_id": new_answer.author_id
        }

        # Send notification to the author of the question

        question_author = r.get(f"question_{new_answer.question_id}")
        author_email = r.get(f"user_{question_author}")

        print(author_email)

        notification = {
            "recipient_email": author_email,
            "subject": "They answered your question!",
            "body": f"{new_answer.body}"
        }

        notification_response = requests.post("http://localhost:8004/notification/send-notification", json=notification)
        message['notification_status'] = notification_response.status_code

    return message

def get_answer_by_id(answer_id):
    answer = Answer.query.get(answer_id)

    message = {
        "id": answer.id,
        "body": answer.body,
        "is_final": answer.is_final,
        "question_id": answer.question_id,
        "author_id": answer.author_id
    }

    return message

def get_all_answers():
    answers = Answer.query.all()

    message = {}

    for answer in answers:
        message[answer.id] = {
            "id": answer.id,
            "body": answer.body,
            "is_final": answer.is_final,
            "question_id": answer.question_id,
            "author_id": answer.author_id
        }

    return message

def set_final_answer_by_id(answer_id):
    answer = Answer.query.get(answer_id)

    answer.is_final = True
    db.session.commit()

    request = requests.patch(f"http://localhost:8000/questions/resolve/{answer.question_id}")
    print(request.text, request.status_code)
    
    message = {
        "id": answer.id,
        "body": answer.body,
        "is_final": answer.is_final,
        "question_id": answer.question_id,
        "author_id": answer.author_id
    }

    author = requests.get(f"http://localhost:8003/auth/get_one/{answer.author_id}").json()

    author_email = author['email']
    
    notification = {
        "recipient_email": author_email,
        "subject": "Your answer was marked as final!",
        "body": f"{answer.body}"
    }

    notification_response = requests.post("http://localhost:8004/notification/send-notification", json=notification)
    message['notification_status'] = notification_response.status_code

    return message

def is_final_by_id(answer_id):
    answer = Answer.query.get(answer_id)

    message = {
        "is_final": answer.is_final
    }

    return message

def delete_answer_by_id(answer_id):
    answer = Answer.query.get(answer_id)

    db.session.delete(answer)
    db.session.commit()

    message = {
        "message": "Answer deleted"
    }

    return message

def delete_all_answers():
    answers = Answer.query.all()

    for answer in answers:
        db.session.delete(answer)
        db.session.commit()

    message = {
        "message": "All answers deleted"
    }

    return message