from unicodedata import decomposition
from flask_restx import Namespace, fields


class UserDto:
    """The user dto"""

    api = Namespace("user", description="user related operations")
    user = api.model(
        "user",
        {
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
            "password": fields.String(required=True, description="user password"),
        },
    )

    user_role = api.model(
        "user_role",
        {
            "user_id": fields.Integer(required=True, description="user id"),
            "role_id": fields.Integer(required=True, description="role id"),
        },
    )
