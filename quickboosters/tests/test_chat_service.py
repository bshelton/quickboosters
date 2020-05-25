from __future__ import annotations
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from quickboosters.tests.fixtures import app
from quickboosters.tests.fixtures import db

from quickboosters.api.roles.enums import RoleTypes

from quickboosters.api.chat.model import ChatLog, ChatRoom
from quickboosters.api.chat.interface import ChatLogInterface
from quickboosters.api.chat.interface import ChatRoomInterface

from quickboosters.api.chat.service import ChatLogService
from quickboosters.api.chat.service import ChatRoomService

from quickboosters.api.users.model import User
from quickboosters.api.users.interface import UserInterface
from quickboosters.api.users.service import UserService


def create_user() -> User:
    """ Nessecary for ForeignKey Constraint"""
    user: UserInterface = {
        "user_id": 1,
        "username": "exampleName",
        "email": "example@example.com",
        "password": "password",
        "role": RoleTypes.MEMBER,
        "created_on": datetime.now()
    }

    return UserService().create(user)


def create_room_interface() -> ChatRoomInterface:
    room: ChatRoomInterface = {
        "room_id": 1,
        "room_name": "exampleName"
    }
    return room


def create_room() -> None:

    room: ChatRoomInterface = {
        "room_id": 1,
        "room_name": "exampleRoom"
    }
    return ChatRoomService().create(room)


def create_log() -> None:
    log: ChatLogInterface = {
        "log_id": 1,
        "message": "exampleMessage",
        "userfrom": "exampleName",
        "created_data": datetime.now(),
        "room_name": "exampleRoom"
    }
    return ChatLogService().create(log)


def test_create_room(db: SQLAlchemy) -> None:
    assert create_room().room_id == 1


def test_create_log(db: SQLAlchemy) -> None:
    room: ChatRoom = create_room()
    user: User = create_user()
    log: ChatLog = create_log()

    assert log.log_id == 1


def test_delete_room(db: SQLAlchemy) -> None:
    assert ChatRoomService().delete_by_id(create_room().room_id).room_id == 1


def test_delete_log(db: SQLAlchemy) -> None:
    create_room()
    create_user()
    assert ChatLogService().delete_by_id(create_log().log_id).log_id == 1


def test_update_room(db: SQLAlchemy) -> None:
    room: ChatRoom = create_room()
    changes: ChatRoomInterface = create_room_interface()
    changes["room_name"] = "updatedName"
    updated_room: ChatRoom = ChatRoomService().update(room, changes)

    assert updated_room.room_name == "updatedName"
