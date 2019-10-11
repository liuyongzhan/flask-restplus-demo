import os
from . import db
from . import dev_db

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (
        dev_db.MYSQL_USERNAME, dev_db.MYSQL_PASSWORD, dev_db.MYSQL_HOST, dev_db.MYSQL_PORT, dev_db.MYSQL_DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (
        dev_db.MYSQL_USERNAME, dev_db.MYSQL_PASSWORD, dev_db.MYSQL_HOST, dev_db.MYSQL_PORT, dev_db.MYSQL_DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (
        db.MYSQL_USERNAME, db.MYSQL_PASSWORD, db.MYSQL_HOST, db.MYSQL_PORT, db.MYSQL_DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
