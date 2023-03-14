import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "_&xgpaf_@-(6c#_n6eqb9(it947^!7x1c5lylhru9yrixyn2h!"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'darkly'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass

