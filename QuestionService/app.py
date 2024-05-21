from flask import Flask
from questions.routes import questions_bp
from extensions import initialize_extensions, db
from config import Config

def create_app():
    api = Flask(__name__)
    api.config.from_object(Config)
    api.register_blueprint(questions_bp)
    initialize_extensions(api)

    with api.app_context():
        db.create_all()

    return api

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)