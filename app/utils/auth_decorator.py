from flask import request
from functools import wraps

from app.utils.auth_helper import AuthHelper


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = AuthHelper.get_auth_info(current_request=request)
        token = data.get("data")

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated
