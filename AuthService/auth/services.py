from flask_jwt_extended import create_access_token
import bcrypt

from auth.models import User
from extensions import db


def register_user(email, password):
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return None, 'User already exists'

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

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
