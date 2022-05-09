from flask_restx import Namespace, fields


class RoleDto:
    """The role dto"""

    api = Namespace("role", description="role related operations")
    role = api.model(
        "role",
        {
            "role_name": fields.String(required=True, description="role name"),
        },
    )
