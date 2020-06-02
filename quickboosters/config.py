from dotenv import load_dotenv
import os


class Config(object):
    project_folder = os.path.dirname(os.path.realpath(__file__))
    static_folder = os.path.join(project_folder + '/frontend/static')
    template_folder = os.path.join(project_folder + '/frontend/templates')
    DEBUG = True
    load_dotenv(os.path.join(project_folder + '/env_files/', '.env'))
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET = os.getenv('JWT_SECRET')
    DB_USER = ''
    DB_PASS = ''
    DB_HOST = ''
    DB_NAME = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'

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
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SMTP_SERVER = "localhost"
    SMTP_PORT = 8025
    SENDER_EMAIL = "noreply@quickboosters.com"
    DB_USER = os.getenv('DB_USER_PROD')
    DB_PASS = os.getenv('DB_PASS_PROD')
    DB_HOST = os.getenv('DB_HOST_PROD')
    DB_NAME = os.getenv('DB_NAME_PROD')

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return 'mysql://{0}:{1}@{2}/{3}'.format(
            self.DB_USER,
            self.DB_PASS,
            self.DB_HOST,
            self.DB_NAME
        )


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SMTP_SERVER = "localhost"
    # SMTP_PORT = 8025
    # SENDER_EMAIL = "noreply@quickboosters.com"
    DB_USER = os.getenv('DB_USER_TEST')
    DB_PASS = os.getenv('DB_PASS_TEST')
    DB_HOST = os.getenv('DB_HOST_TEST')
    DB_NAME = os.getenv('DB_NAME_TEST')

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


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SMTP_SERVER = "localhost"
    SMTP_PORT = 8025
    SENDER_EMAIL = "noreply@quickboosters.com"
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
