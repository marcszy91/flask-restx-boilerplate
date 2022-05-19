from flask import current_app

from app.utils.auth_ldap import LDAPHelper

from .. import logger
from app.model import User
from app.service.blacklist_token import save_blacklist_token
from app.service.user import save_new_user
from app.utils.auth_helper import AuthHelper
from typing import Dict, List


def login_user(data: Dict[str, str]) -> List:
    """login user

    Returns:
        List[]: response object
    """
    try:
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        user = User.query.filter_by(username=data.get("username")).first()
        auth_type = current_app.config["AUTH_TYPE"]
        # if auth type is ldap and user not exist
        # create user if ldap credentials are valid
        if auth_type == "LDAP" and not user:
            ldap_email = LDAPHelper.ldap_get_email_by_username(
                username=username, password=password
            )
            if ldap_email is not None:
                user = User(email=email, username=username, password=password)
                data["email"] = email
                save_new_user(data=data)
        if user and user.check_password(password=password, auth_type=auth_type):
            auth_token = AuthHelper.encode_auth_token(username=user.username)
            if auth_token:
                response_object = {
                    "status": "success",
                    "message": "Successfully logged in.",
                    "Authorization": auth_token,
                }
                return response_object, 200
        else:
            logger.error("Login failed for user %s", username)
            response_object = {
                "status": "fail",
                "message": "username or password does not match",
            }
            return response_object, 401
    except Exception as e:
        logger.critical(e)
        response_object = {"status": "fail", "message": "Try again"}
        return response_object, 500


def logout_user(auth_token: str):
    """Logout user

    Args:
        auth_token (str): the token

    Returns:
        dict[str, str], int: The response object, status code
    """
    if auth_token:
        payload = AuthHelper.decode_auth_token(auth_token)
        user = User.query.filter_by(username=payload).first()
        if user:
            return save_blacklist_token(token=auth_token)
        else:
            response_object = {"status": "fail", "message": payload}
            return response_object, 401
    else:
        response_object = {"status": "fail", "message": "Provide a valid auth token."}
        return response_object, 403
