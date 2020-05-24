from __future__ import annotations
import datetime

from quickboosters import db
from quickboosters.config import Config
from quickboosters.api.users.interface import UserInterface


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from time import time
import jwt


class User(UserMixin, db.Model):
    """A user within the app"""

    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column("password", String(255), nullable=False)
    created_on = Column(DateTime(), default=datetime.datetime.utcnow, nullable=False)
    role = Column(String(30))
    orders = db.relationship('Order', backref='users')

    def __init__(self, username, email, password, role, created_on):
        self.username = username
        self.email = email
        self._password = generate_password_hash(password)
        self.role = role
        self.created_on = created_on

    def check_password(self, password) -> bool:
        """Checks for a valid password

        Parameters
        ----------
        password: str
            The string to validate.

        Returns:
            bool: The Boolean depending if passwords match.
        """

        return check_password_hash(self._password, password)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, cleartext):
        self._password = generate_password_hash(cleartext)

    def update(self: User, interface: UserInterface) -> User:
        """Update to an existing user with a UserInterface

        Parameters
        ----------
        interface: UserInterface
            The user interface containing the changes to be implemented.

        Returns:
            User: The user with the updated changes.
        """

        for key, val in interface.items():
            setattr(self, key, val)
        return self

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.user_id, 'exp': time() + expires_in},
            Config().SECRET_KEY, algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token) -> User:
        try:
            user_id = jwt.decode(token, Config().SECRET_KEY,
                                 algorithms=['HS256'])['reset_password']
            return User.query.get(user_id)
        except Exception as e:
            return str(e)
