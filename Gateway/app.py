from flask import Flask
from services.auth.routes import auth_bp
from services.questions.routes import questions_bp
from services.answers.routes import answers_bp
from services.notifications.routes import notification_bp


def create_app():
    api = Flask(__name__)
    api.register_blueprint(auth_bp)
    api.register_blueprint(questions_bp)
    api.register_blueprint(answers_bp)
    api.register_blueprint(notification_bp)

    return api

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8005)
