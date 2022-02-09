import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """The Config base class for the flask application"""

    SECRET_KEY = os.getenv(key="SECRET_KEY", default="default_secret_key")
    DEBUG = False


class DevConfig(Config):
    """development config

    Args:
        Config (Config): The base class
    """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "flask_boilerplate.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """test config

    Args:
        Config (Config): The base class
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "flask_boilerplate_test.db"
    )
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """production config

    Args:
        Config (Config): The base class
    """

    DEBUG = False


config_by_name = dict(dev=DevConfig, test=TestConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
