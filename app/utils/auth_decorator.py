from flask import abort, request
from functools import wraps
from typing import List

from app.utils.auth_helper import AuthHelper


def token_required(token_wrapper):
    @wraps(token_wrapper)
    def decorated(*args, **kwargs):
        data, status = AuthHelper.get_auth_info(current_request=request)
        token = data.get("data")

        if not token:
            return abort(status, data)

        return token_wrapper(*args, **kwargs)

    return decorated


def role_required(roles: List):
    def wrap(parent_function):
        def decorated(*args, **kwargs):
            data, status = AuthHelper.check_user_roles(
                current_request=request, roles=roles
            )
            role = data.get("data")

            if not role:
                return abort(status, data)

            return parent_function(*args, **kwargs)

        return decorated

    return wrap
