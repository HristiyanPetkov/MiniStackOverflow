from flask_jwt_extended import create_access_token
import bcrypt
import redis

from auth.models import User
from extensions import db

# Create a connection to the Redis server with database name cache-LVFMKUIY
host = 'redis-19916.c250.eu-central-1-1.ec2.redns.redis-cloud.com'
port = 19916
password = "cWjOTj69Lk2mGiMs9O9aKI2SRJ5lnubm"

# Connect to the Redis server
r = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

def register_user(email, password):
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return None, 'User already exists'

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    user_key = f"user_{new_user.id}"
    r.set(user_key, new_user.email)

    return new_user, None


def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return None, 'User not found'

    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return None, 'Invalid password'

    return user, None


def generate_access_token(user_id):
    return create_access_token(identity=user_id)

def get_user_by_id(user_id):
    user = User.query.get(user_id)

    message = {
        "id": user.id,
        "email": user.email
    }

    return message