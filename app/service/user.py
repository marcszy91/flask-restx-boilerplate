from typing import Dict, List, Tuple

from app import db
from app.model import User


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    """save new user object in database

    Args:
        data (Dict[str, str]): Dictionary with username and email

    Returns:
        Tuple[Dict[str, str], int]: the response object and a status code
    """
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        new_user = User(email=data["email"], username=data["username"])
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
        [type]: [description]
    """
    return User.query.filter_by(email=email).first()


def save_changes(user: User) -> None:
    """save user to database

    Args:
        data (User): the user object
    """
    db.session.add(user)
    db.session.commit()
