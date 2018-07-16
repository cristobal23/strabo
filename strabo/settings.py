import os
import tempfile

db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = os.environ['APP_SECRET_KEY']


class ProdConfig(Config):
    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    CACHE_TYPE = 'simple'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/strabo')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = 'null'
    CACHE_NO_NULL_WARNING = True
    ASSETS_DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = 'null'
    CACHE_NO_NULL_WARNING = True
    WTF_CSRF_ENABLED = False
