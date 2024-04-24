import requests
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from helper_functions.jwt_helper import getUserFromToken

answers_bp = Blueprint('answers', __name__, url_prefix='/answers')

ANSWERS_SERVICE_URL = 'http://answers-service:8000/answers'


@answers_bp.route('/create', methods=['POST'])
@jwt_required()
def create_answer():
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    request.json['author_id'] = response.json()['user_id']

    response = requests.post(f'{ANSWERS_SERVICE_URL}/create', json=request.json)

    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify(response.json()), response.status_code


@answers_bp.route('/get_one/<int:answer_id>', methods=['GET'])
def get_answer(answer_id):
    response = requests.get(f'{ANSWERS_SERVICE_URL}/get_one/{answer_id}')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@answers_bp.route('/get_all', methods=['GET'])
def get_all_answers():
    response = requests.get(f'{ANSWERS_SERVICE_URL}/get_all')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@answers_bp.route('/set_final/<int:answer_id>', methods=['PATCH'])
@jwt_required()
def set_final_answer(answer_id):
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    request.json['author_id'] = response.json()['user_id']

    response = requests.patch(f'{ANSWERS_SERVICE_URL}/set_final/{answer_id}', json=request.json)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@answers_bp.route('/is_final/<int:answer_id>', methods=['GET'])
def is_final_answer(answer_id):
    response = requests.get(f'{ANSWERS_SERVICE_URL}/is_final/{answer_id}')

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@answers_bp.route('/delete_one/<int:answer_id>', methods=["DELETE"])
@jwt_required()
def delete_answer(answer_id):
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    response = requests.delete(f'{ANSWERS_SERVICE_URL}/delete_one/{answer_id}', headers=request.headers)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@answers_bp.route('/delete_all', methods=["DELETE"])
@jwt_required()
def delete_all_answers():
    response = getUserFromToken()

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    response = requests.delete(f'{ANSWERS_SERVICE_URL}/delete_all', headers=request.headers)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code