from .. import db
import datetime


class BlacklistToken(db.Model):
    """Blacklist jwt tokens"""

    __tablename__ = "blacklist_token"
    token_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    insert_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.insert_date = datetime.datetime.now()

    def __repr__(self):
        return "<id: token: {}".format(self.token)

    @staticmethod
    def check_blacklist(token: str):
        """check if token is on blacklist

        Args:
            token (str): the auth token

        Returns:
            bool: True if is blacklist otherwise False
        """
        res = BlacklistToken.query.filter_by(token=str(token)).first()
        if res:
            return True
        else:
            return False
