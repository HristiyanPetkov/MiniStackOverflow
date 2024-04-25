import requests
from flask import jsonify, request, Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

AUTH_SERVICE_URL = 'http://127.0.0.1:8003/auth'


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
def validate_token():
    response = requests.get(f'{AUTH_SERVICE_URL}/validate-token', headers=request.headers)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code
