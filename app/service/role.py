from typing import Dict, List, Tuple

from app import db
from app.model import Role


def save_new_role(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    """save new role object in database

    Args:
        data (Dict[str, str]): Dictionary with rolename

    Returns:
        Tuple[Dict[str, str], int]: the response object and a status code
    """
    role = Role.query.filter_by(role_name=data["role_name"]).first()
    if not role:
        new_role = Role(role_name=data["role_name"])
        save_changes(role=new_role)
        response_object = {"status": "success", "message": "Successfully added role."}
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Role already exists",
        }
        return response_object, 409


def get_all_roles() -> List[Role]:
    """get all roles

    Returns:
        [Role]: a list of all roles
    """
    return Role.query.all()


def save_changes(role: Role) -> None:
    """save role to database

    Args:
        role (Role): the role object
    """
    db.session.add(role)
    db.session.commit()
