from __future__ import annotations

from quickboosters import db
from quickboosters.api.users.interface import UserInterface

from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):
    """A user within the app"""

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    role = relationship("Role")
    created_on = Column(DateTime(), nullable=False)

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
