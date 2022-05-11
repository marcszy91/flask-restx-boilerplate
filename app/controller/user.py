from flask import request
from flask_restx import Resource
from typing import Dict, Tuple

from ..dto.user import UserDto
from ..service.user import save_new_user, get_all_users, get_a_user, add_user_role
from app.utils.auth_decorator import token_required

api = UserDto.api
_user = UserDto.user
_user_role = UserDto.user_role


@api.route("/")
class UserList(Resource):
    """route to list all users and create a new user

    Args:
        Resource (UserDto.user): the user dto

    Returns:
        [User]: List of users
    """

    @api.doc("list_of_registered_users", security="apikey")
    @api.marshal_list_with(_user, envelope="data")
    @token_required
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    def post(self) -> Tuple[Dict[str, str], int]:
        """post route to create new user

        Returns:
            Tuple[Dict[str, str], int]: response and status
        """
        data = request.json
        return save_new_user(data=data)


@api.route("/<email>")
@api.param("email", "The User email")
@api.response(404, "User not found.")
class User(Resource):
    """route to get user by email

    Args:
        Resource (str): email

    Returns:
        [User]: the user
    """

    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, email: str):
        """get a user by a email

        Args:
            email (str): the email

        Returns:
            [User]: the user
        """
        user = get_a_user(email=email)
        if not user:
            return api.abort(404)
        else:
            return user


@api.route("/role")
class UserRole(Resource):
    """route to handle userole

    Args:
        Resource (str): the user_role dto

    Returns:
        [UserRole]: the user role
    """

    @api.expect(_user_role, validate=True)
    @api.response(201, "user role successfully added.")
    @api.doc("add role to user")
    def post(self) -> Tuple[Dict[str, str], int]:
        """post route to add role to user

        Returns:
            Tuple[Dict[str, str], int]: response and status
        """
        data = request.json
        return add_user_role(data=data)
