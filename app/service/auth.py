from .. import logger
from app.dto.user import UserDto
from app.model import User
from app.utils.auth_helper import AuthHelper
from typing import Dict, List


def login_user(data: Dict[str, str]) -> List:
    """login user

    Returns:
        List[]: response object
    """
    try:
        user = User.query.filter_by(username=data.get("username")).first()
        if user and user.check_password(password=data.get("password")):
            auth_token = AuthHelper.encode_auth_token(username=user.username)
            if auth_token:
                response_object = {
                    "status": "success",
                    "message": "Successfully logged in.",
                    "Authorization": auth_token,
                }
                return response_object, 200
        else:
            logger.error("Login failed for user %s", data.get("username"))
            response_object = {
                "status": "fail",
                "message": "email or password does not match",
            }
            return response_object, 401
    except Exception as e:
        logger.critical(e)
        response_object = {"status": "fail", "message": "Try again"}
        return response_object, 500
