from flask import request
from flask_restx import Resource

from ..service.auth import login_user, logout_user
from ..dto.auth import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route("/login")
class UserLogin(Resource):
    """
    User Login Resource
    """

    @api.doc("user login")
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return login_user(data=post_data)


@api.route("/logout")
class UserLogout(Resource):
    """
    User Logout Resource
    """

    @api.doc("user logout", security="apikey")
    def post(self):
        """Logout user"""
        auth_token = request.headers.get("X-API-KEY")
        return logout_user(auth_token=auth_token)
