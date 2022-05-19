import logging
import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.engine import Engine
from sqlalchemy import event

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app() -> Flask:
    """Create the flask app
    Returns:
        Flask: The flask app object
    """
    # create flask app
    app = Flask(__name__)

    # Load env
    config_name = os.getenv(key="CONFIG_NAME", default="dev")

    # get config object
    config = config_by_name[config_name]
    app.config.from_object(obj=config)

    # load additional configs from env
    load_config_from_env(app=app)

    # initialize sql alchemy
    db.init_app(app=app)

    # initialie brcypt
    flask_bcrypt.init_app(app=app)

    return app


def init_logger() -> logging.Logger:
    """initialze the main logger"""
    login_level_name = os.getenv(key="LOG_LEVEL", default="CRITICAL")
    login_level = logging.getLevelName(level=login_level_name)
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s")
    stream_heandler = logging.StreamHandler()
    stream_heandler.setFormatter(fmt=formatter)
    logger = logging.getLogger(name="flask-restx-app")
    logger.setLevel(level=login_level)
    logger.addHandler(hdlr=stream_heandler)
    return logger


def load_config_from_env(app: Flask) -> None:
    """load config from env

    Args:
        app (Flask): the flask app object
    """
    # Auth config
    app.config["AUTH_TYPE"] = os.getenv("AUTH_TYPE", "BASIC")
    # LADP config
    if app.config["AUTH_TYPE"] == "LDAP":
        app.config["LDAP_HOST"] = os.getenv("LDAP_HOST")
        app.config["LDAP_USER_PREFIX"] = os.getenv("LDAP_USER_PREFIX")
        app.config["LDAP_SEARCH_BASE"] = os.getenv("LDAP_SEARCH_BASE")
        app.config["LDAP_SEARCH_FILTER"] = os.getenv("LDAP_SEARCH_FILTER")


# set foreign keys on for sqlite connection
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


logger = init_logger()
app = create_app()
