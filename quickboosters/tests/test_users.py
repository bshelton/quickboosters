from __future__ import annotations
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from quickboosters.tests.fixtures import app
from quickboosters.tests.fixtures import db

from quickboosters.api.roles.enums import RoleTypes
from quickboosters.api.users.model import User
from quickboosters.api.users.interface import UserInterface
from quickboosters.api.users.service import UserService


def create_user() -> User:
    user: UserInterface = {
        "user_id": 1,
        "username": "exampleUserName",
        "email": "example@example.com",
        "password": "password",
        "role": RoleTypes.MEMBER,
        "created_on": datetime.now()
    }

    new_user = UserService().create(user)
    return new_user


def test_get_user_by_id(db: SQLAlchemy) -> None:
    new_user = create_user()
    assert UserService.get_by_id(new_user.user_id).user_id == 1


def test_get_user_by_username(db: SQLAlchemy) -> None:
    new_user = create_user()
    assert UserService.get_by_username(
           new_user.username).username == "exampleUserName"


def test_create_user(db: SQLAlchemy) -> None:
    new_user = create_user()
    assert new_user


def test_delete_user(db: SQLAlchemy) -> None:
    new_user = create_user()

    deleted_user = UserService().delete_by_id(new_user.user_id)

    if deleted_user:
        assert len(UserService().get_all()) == 0


def test_update_user(db: SQLAlchemy) -> None:
    new_user = create_user()

    new_changes = UserInterface()
    new_changes['username'] = 'updatedName'

    updated_user: User = UserService().update(new_user, new_changes)

    assert updated_user.username == 'updatedName'
