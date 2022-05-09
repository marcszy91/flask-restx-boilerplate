from .. import db


class Role(db.Model):
    """Role Model for storing roles"""

    __tablename__ = "role"

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), unique=True)
    user_roles = db.relationship("UserRole", cascade="all, delete")
