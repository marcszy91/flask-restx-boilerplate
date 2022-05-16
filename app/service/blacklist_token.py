from typing import Dict, List, Tuple

from app import db
from app import logger
from app.model import BlacklistToken


def save_blacklist_token(token: str) -> Tuple[Dict[str, str], int]:
    blacklist_token = BlacklistToken(token=token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {"status": "success", "message": "Successfully logged out."}
        return response_object, 200
    except Exception as e:
        logger.critical(e)
        response_object = {"status": "fail", "message": "Logout failed"}
        return response_object, 200
