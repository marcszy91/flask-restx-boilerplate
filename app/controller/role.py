from flask import request
from flask_restx import Resource
from typing import Dict, Tuple

from ..dto.role import RoleDto
from ..service.role import save_new_role, get_all_roles

api = RoleDto.api
_role = RoleDto.role


@api.route("/")
class RoleList(Resource):
    """route to list all roles and create a new role

    Args:
        Resource (UserDto.role): the role dto

    Returns:
        [Roles]: List of Roles
    """

    @api.doc("list_of_roles")
    @api.marshal_list_with(_role, envelope="data")
    def get(self):
        """List all roles"""
        return get_all_roles()

    @api.expect(_role, validate=True)
    @api.response(201, "Role successfully created.")
    @api.doc("create a new role")
    def post(self) -> Tuple[Dict[str, str], int]:
        """post route to create new role

        Returns:
            Tuple[Dict[str, str], int]: response and status
        """
        data = request.json
        return save_new_role(data=data)
