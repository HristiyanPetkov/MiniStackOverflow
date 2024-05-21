import requests
from flask import request, jsonify

AUTH_SERVICE_URL = 'http://127.0.0.1:8003/auth'


def getUserFromToken():
    response = requests.get(f'{AUTH_SERVICE_URL}/validate-token', headers=request.headers)

    return response