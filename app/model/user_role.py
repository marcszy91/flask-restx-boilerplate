from .. import db


class UserRole(db.Model):
    """UserRole Model for storing user roles"""

    __tablename__ = "user_role"

    user_id = db.Column(
        db.ForeignKey("user.user_id"),
        primary_key=True,
    )
    role_id = db.Column(
        db.ForeignKey("role.role_id"),
        primary_key=True,
    )

    role = db.relationship("Role", foreign_keys=[role_id])
