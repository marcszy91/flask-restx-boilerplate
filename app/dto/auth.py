from flask_restx import Namespace, fields


class AuthDto:
    """The auth dto"""

    api = Namespace("auth", description="authentication related operations")
    user_auth = api.model(
        "auth_details",
        {
            "username": fields.String(required=True, description="user name"),
            "password": fields.String(required=True, description="user password"),
        },
    )
