import os

from dotenv import load_dotenv

from src.dataclass.database_dataclass import DatabaseDataclass
from src.dataclass.kaggle_dataclass import KaggleDataclass

load_dotenv()

def get_kaggle_config():
    kaggle_api_key = os.getenv('KAGGLE_API_KEY')

    if kaggle_api_key is None:
        raise Exception(
            "Missing Kaggle API key in environment"
        )


    return KaggleDataclass(kaggle_api_key)

def get_database_config():

    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')

    if db_user is None or db_password is None or db_host is None or db_name is None:
        raise Exception(
            "Missing database credentials in environment, check if DB_USER, DB_PASSWORD, DB_HOST, DB_NAME are set in .env file"
        )

    return DatabaseDataclass(db_user, db_password, db_host, db_name)