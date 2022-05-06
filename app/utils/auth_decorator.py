from flask import request
from functools import wraps

from app.utils.auth_helper import AuthHelper


def token_required(token_wrapper):
    @wraps(token_wrapper)
    def decorated(*args, **kwargs):
        data, status = AuthHelper.get_auth_info(current_request=request)
        token = data.get("data")

        if not token:
            return data, status

        return token_wrapper(*args, **kwargs)

    return decorated
