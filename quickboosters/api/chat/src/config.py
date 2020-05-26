from dotenv import load_dotenv
import os


class Config(object):
    project_folder = os.path.dirname(os.path.realpath(__file__))
    env_file = os.path.join(project_folder + '/.env')
    DEBUG = True
    load_dotenv(os.path.join(project_folder + '/.env'))
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_USER = os.getenv('DB_USER_PROD')
    DB_PASS = os.getenv('DB_PASS_PROD')
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME_PROD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return 'mysql://{0}:{1}@{2}/{3}'.format(
            self.DB_USER,
            self.DB_PASS,
            self.DB_HOST,
            self.DB_NAME
        )
