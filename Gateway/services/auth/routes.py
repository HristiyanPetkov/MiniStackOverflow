import requests
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

AUTH_SERVICE_URL = 'http://auth-service:8000/auth'


@auth_bp.route('/register', methods=['POST'])
def register():
    response = requests.post(f'{AUTH_SERVICE_URL}/register', json=request.json)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@auth_bp.route('/login', methods=['POST'])
def login():
    response = requests.post(f'{AUTH_SERVICE_URL}/login', json=request.json)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code


@auth_bp.route('validate-token', methods=['GET'])
@jwt_required()
def validate_token():
    response = requests.get(f'{AUTH_SERVICE_URL}/validate-token', headers=request.headers)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code
