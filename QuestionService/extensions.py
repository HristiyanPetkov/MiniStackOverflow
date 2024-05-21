from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_extensions(app):
    db.init_app(app)