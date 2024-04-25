import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'mysql+mysqlconnector://root:password@mysql/microservice_auth'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'KGe2j5oq5uWbXkLXjGNZ6VGsPhJf2UzE'
