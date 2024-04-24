from flask import Blueprint, request, jsonify

from notifications.services import send_email_notification

notification_bp = Blueprint('notification', __name__, url_prefix='/notification')

@notification_bp.route('/send-notification', methods=['POST'])
def send_notification():
    data = request.json
    recipient_email = data.get('recipient_email')
    body = data.get('body')

    if not recipient_email or not body:
        return jsonify({'message': 'Recipient email and body are required'}), 400

    success, error_message = send_email_notification(recipient_email, body)

    if success:
        return jsonify({'message': 'Notification sent successfully'}), 200
    else:
        return jsonify({'message': f'Failed to send notification: {error_message}'}), 500
