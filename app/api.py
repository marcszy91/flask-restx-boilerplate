from flask_restx import Api, Namespace
from flask import Blueprint

import app.controller

blueprint = Blueprint("api", __name__)

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "X-API-KEY"}}

api = Api(
    blueprint,
    title="FLASK REST-X API BOILER-PLATE",
    version="1.0",
    description="a boilerplate for a flask rest-x api",
    authorizations=authorizations,
)

for namespace in vars(app.controller).values():
    if isinstance(namespace, Namespace):
        api.add_namespace(namespace, path=namespace.path)
