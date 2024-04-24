import requests
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from helper_functions.jwt_helper import getUserFromToken

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

QUESTIONS_SERVICE_URL = 'http://questions-service:8000/questions'


@questions_bp.route('/create', methods=['POST'])
@jwt_required()
def create_question():
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    request.json['author_id'] = response.json()['user_id']

    response = requests.post(f'{QUESTIONS_SERVICE_URL}/create', json=request.json)

    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify(response.json()), response.status_code


@questions_bp.route('/get_one/<int:question_id>', methods=['GET'])
def get_question(question_id):
    response = requests.get(f'{QUESTIONS_SERVICE_URL}/get_one/{question_id}')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@questions_bp.route('/get_all', methods=['GET'])
def get_all_questions():
    response = requests.get(f'{QUESTIONS_SERVICE_URL}/get_all')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@questions_bp.route('/resolve/<int:question_id>', methods=['PATCH'])
@jwt_required()
def resolve_question(question_id):
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    request.json['author_id'] = response.json()['user_id']

    response = requests.patch(f'{QUESTIONS_SERVICE_URL}/resolve/{question_id}', json=request.json)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@questions_bp.route('/is_resolved/<int:question_id>', methods=['GET'])
def is_resolved(question_id):
    response = requests.get(f'{QUESTIONS_SERVICE_URL}/is_resolved/{question_id}')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@questions_bp.route('/delete_one/<int:question_id>', methods=['DELETE'])
@jwt_required()
def delete_question(question_id):
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    response = requests.delete(f'{QUESTIONS_SERVICE_URL}/delete_one/{question_id}')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@questions_bp.route('/delete_all', methods=['DELETE'])
@jwt_required()
def delete_all_questions():
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    response = requests.delete(f'{QUESTIONS_SERVICE_URL}/delete_all')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code
