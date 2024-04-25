import os

class Config:
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:password@mysql/microservice-answers'

if __name__ == '__main__':
    config = Config()