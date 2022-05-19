from .. import db, flask_bcrypt
from app.enum.auth_type import AuthType

from app.utils.auth_ldap import LDAPHelper


class User(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    user_roles = db.relationship("UserRole")

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

    def check_password(self, password: str, auth_type: str):
        """check password

        Args:
            password (str): the password
            auth_type (str): the auth type

        Returns:
            _type_: True if login successed otherwise False
        """
        if auth_type == AuthType.BASIC.value:
            return flask_bcrypt.check_password_hash(self.password_hash, password)
        elif auth_type == AuthType.LDAP.value:
            return LDAPHelper.ldap_auth(username=self.username, password=password)
        else:
            return False
