from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from auth.services import *

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user, error = register_user(email, password)

    if error:
        return jsonify({'message': error}), 400

    access_token = create_access_token(user.id)

    return jsonify({'access_token': access_token}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user, error = login_user(email, password)

    if error:
        return jsonify({'message': error}), 400

    access_token = create_access_token(user.id)

    return jsonify({'access_token': access_token}), 200


@auth_bp.route('/validate-token', methods=['GET'])
@jwt_required()
def validate_token():
    current_user_id = get_jwt_identity()
    if not current_user_id:
        return jsonify({'message': 'Invalid token'}), 400

    return jsonify({'user_id': {current_user_id}}), 200

@auth_bp.route('/get_one/<int:id>', methods=['GET'])
def get_one(id):
    user = get_user_by_id(id)
    return jsonify(user), 200