import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

db = SQLAlchemy()


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

    return app


app = create_app()
