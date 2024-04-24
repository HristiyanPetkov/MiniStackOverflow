import requests
from flask import request, jsonify

AUTH_SERVICE_URL = 'http://auth-service:8000/auth'


def getUserFromToken():
    response = requests.get(f'{AUTH_SERVICE_URL}/validate-token', headers=request.headers)

    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    return response.json()