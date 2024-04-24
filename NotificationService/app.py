from flask import Flask
from notifications.routes import notification_bp
#from config import Config

def create_app():
    api = Flask(__name__)
    #api.config.from_object(Config)
    api.register_blueprint(notification_bp)

    return api

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)