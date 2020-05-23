from typing import List

from quickboosters.api.users.interface import UserInterface
from quickboosters.api.users.schema import UserSchema
from quickboosters.api.users.model import User

from quickboosters import db


class UserService:
    """Service for dealing with users."""

    @staticmethod
    def get_all() -> List[User]:
        """Retrieve all users.

        Returns:
            List[User]: a list of users.
        """
        return User.query.all()

    @staticmethod
    def get_by_id(user_id: int) -> User:
        """Retrieve one user matching a given id.

        Returns:
            User: one user with id given
        """
        return User.query.get(user_id)

    @staticmethod
    def get_by_username(username: str) -> User:
        """Retrieve one user matching a given username.

        Returns:
            User: one user with username given
        """
        return User.query.filter(User.username == username).first()

    @staticmethod
    def get_by_email(email: str) -> User:
        """Retrieve one user matching a given email.

        Returns:
            User: One user with email given
        """
        return User.query.filter(User.email == email).first()

    @staticmethod
    def create(attributes: UserSchema) -> User:
        """Creates a new user.

        Parameters
        ----------
        attributes : UserInterface
            The attributes of a new user.

        Returns:
            User: The newly created user.
        """

        user: User = User(username=attributes["username"],
                          email=attributes["email"],
                          password=attributes["password"],
                          role=attributes["role"],
                          created_on=attributes["created_on"])

        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update(user: User, changes: UserInterface) -> User:
        """Update to an existing user with a UserInterface

        Parameters
        ----------
        user: User
            The user to update.
        changes: UserInterface
            The updates to the user.

        Returns:
            User: The user with the updated changes.
        """
        user.update(changes)
        db.session.commit()
        return user

    @staticmethod
    def delete_by_id(user_id: int) -> User:
        """Deletes a single user by id

        Parameters
        ----------
        user_id: int
            The user to delete

        Returns:
            User: The user that was deleted
        """

        user: User = User.query.filter(User.id == user_id).first()
        if not user:
            return ""
        db.session.delete(user)
        db.session.commit()
        return user
