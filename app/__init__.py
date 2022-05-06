import logging
import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

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


logger = init_logger()
app = create_app()
