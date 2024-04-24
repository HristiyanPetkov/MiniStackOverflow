import requests
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

notification_bp = Blueprint('notification', __name__, url_prefix='/notification')

NOTIFICATION_SERVICE_URL = 'http://notification-service:8000/notification'


@notification_bp.route('/send-notification', methods=['POST'])
@jwt_required()
def send_notification():
    response = requests.post(f'{NOTIFICATION_SERVICE_URL}/send-notification', json=request.json)

    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify(response.json()), response.status_code
