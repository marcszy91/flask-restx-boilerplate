from flask_restx import Api
from flask import Blueprint

from .controller.user import api as user_namespace

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="FLASK REST-X API BOILER-PLATE",
    version="1.0",
    description="a boilerplate for a flask rest-x api",
)

# add namespace for each api here
api.add_namespace(user_namespace, path="/user")
