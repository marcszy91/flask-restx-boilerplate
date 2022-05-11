from typing import Dict, List, Tuple

from app import db
from app.model import User, UserRole


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    """save new user object in database

    Args:
        data (Dict[str, str]): Dictionary with username and email

    Returns:
        Tuple[Dict[str, str], int]: the response object and a status code
    """
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        new_user = User(
            email=data["email"], username=data["username"], password=data["password"]
        )
        save_changes(user=new_user)
        response_object = {"status": "success", "message": "Successfully registered."}
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users() -> List[User]:
    """get all users

    Returns:
        [User]: a list of all users
    """
    return User.query.all()


def get_a_user(email: str) -> User:
    """get an user by email

    Args:
        email (str): the email

    Returns:
        [User]: the user object
    """
    return User.query.filter_by(email=email).first()


def add_user_role(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    """save new role for user

    Args:
        data (Dict[str, str]): dictionary with user id and role id

    Returns:
        Tuple[Dict[str, str], int]: the response object and a status code
    """
    user_role = UserRole.query.filter_by(
        role_id=data["role_id"], user_id=data["user_id"]
    ).first()
    if not user_role:
        new_user_role = UserRole(role_id=data["role_id"], user_id=data["user_id"])
        save_user_role_changes(user_role=new_user_role)
        response_object = {
            "status": "success",
            "message": "Successfully saved user role.",
        }
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Role already exists",
        }
        return response_object, 409


def save_changes(user: User) -> None:
    """save user to database

    Args:
        data (User): the user object
    """
    db.session.add(user)
    db.session.commit()


def save_user_role_changes(user_role: UserRole) -> None:
    """save user tole to database

    Args:
        user_role (UserRole): the user role object
    """
    db.session.add(user_role)
    db.session.commit()
