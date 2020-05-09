from dotenv import load_dotenv
import os


class Config(object):
    project_folder = os.path.expanduser('~/Desktop/quickboosters')
    DEBUG = False
    load_dotenv(os.path.join(project_folder, '.env'))
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_USER = ''
    DB_PASS = ''
    DB_HOST = ''
    DB_NAME = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return 'mysql://{0}:{1}@{2}/{3}'.format(
            self.DB_USER, 
            self.DB_PASS,
            self.DB_HOST,
            self.DB_NAME
        )

    @SQLALCHEMY_DATABASE_URI.setter
    def SQLALCHEMY_DATABASE_URI(self, user, password, host, db_name):
        return 'mysql://{0}:{1}@{2}/{3}'.format(
                user, 
                password,
                host,
                db_name)

class ProductionConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    DB_USER = os.getenv('DB_USER_DEV')
    DB_PASS = os.getenv('DB_PASS_DEV')
    DB_HOST = os.getenv('DB_HOST_DEV')
    DB_NAME = os.getenv('DB_NAME_DEV')
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return 'mysql://{0}:{1}@{2}/{3}'.format(
            self.DB_USER,
            self.DB_PASS,
            self.DB_HOST,
            self.DB_NAME
        )

    def verbose(self):
        msg = """Using the following database variables:
        DB HOST: {}
        DB NAME: {}
        DB_USER: {}
        DB_PASS: {}
        """.format(
            self.DB_HOST,
            self.DB_NAME,
            self.DB_USER,
            self.DB_PASS
        )
        return msg
