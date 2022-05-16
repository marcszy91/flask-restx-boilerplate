import datetime
import jwt

from flask import Request
from typing import List

from app.model.blacklist_token import BlacklistToken

from ..config import key
from app.model.user import User


class AuthHelper:
    @staticmethod
    def encode_auth_token(username: str) -> str:
        """Encode auth token

        Args:
            user_id (string): the user id

        Returns:
            string: the encoded jwt token
        """
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=1, seconds=5),
                "iat": datetime.datetime.utcnow(),
                "sub": username,
            }
            return jwt.encode(payload, key, algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token) -> str:
        """decode auth token

        Args:
            auth_token (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            payload = jwt.decode(auth_token, key, algorithms=["HS256"])
            is_blacklisted = BlacklistToken.check_blacklist(token=auth_token)
            if is_blacklisted:
                return "Token blacklisted. Please log in again."
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."

    @staticmethod
    def get_auth_info(current_request: Request):
        """get auth info from header

        Args:
            current_request (Request): the current request

        Returns:
            response_object: the response object
        """
        auth_token = current_request.headers.get("X-API-KEY")
        if auth_token:
            payload = AuthHelper.decode_auth_token(auth_token=auth_token)
            user = User.query.filter_by(username=payload).first()
            if user:
                response_object = {
                    "status": "success",
                    "data": {
                        "username": user.username,
                        "email": user.email,
                    },
                }
                return response_object, 200
            response_object = {"status": "fail", "message": payload}
            return response_object, 401
        else:
            response_object = {
                "status": "fail",
                "message": "Provide a valid auth token.",
            }
            return response_object, 401

    @staticmethod
    def check_user_roles(current_request: Request, roles: List):
        """check user roles

        Args:
            current_request (Request): the current request
            roles (List): the required roles

        Returns:
            response_object: the response object
        """
        auth_token = current_request.headers.get("X-API-KEY")
        if auth_token:
            payload = AuthHelper.decode_auth_token(auth_token=auth_token)
            user = User.query.filter_by(username=payload).first()
            for user_role in user.user_roles:
                if user_role.role.role_name in roles:
                    response_object = {
                        "status": "success",
                        "data": {
                            "role": user_role.role,
                        },
                    }
                    return response_object, 200
            response_object = {"status": "fail", "message": "Missing user role"}
            return response_object, 403
        else:
            response_object = {
                "status": "fail",
                "message": "Provide a valid auth token.",
            }
            return response_object, 401
