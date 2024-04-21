import os

class Config:
    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')

    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'