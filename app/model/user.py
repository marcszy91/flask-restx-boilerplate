from .. import db


class User(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "user"

    email = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(50), unique=True)
