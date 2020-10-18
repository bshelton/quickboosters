from __future__ import annotations
import datetime

from quickboosters import db
from quickboosters.api.chat.interface import ChatLogInterface
from quickboosters.api.chat.interface import ChatRoomInterface


class ChatRoom(db.Model):
    __tablename__ = 'chatroom'
    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, room_name):
        self.room_name = room_name

    def update(self: ChatRoom, interface: ChatRoomInterface) -> ChatRoom:
        """Update to an existing room with a ChatRoomInterface

        Parameters
        ----------
        interface: ChatRoomInterface
            The room interface containing the changes to be implemented.

        Returns:
            ChatRoom: The room with the updated changes.
        """

        for key, val in interface.items():
            setattr(self, key, val)
        return self


class ChatLog(db.Model):
    log_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)
    userfrom = db.Column(db.String(20), db.ForeignKey('users.username'), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True))
    room_name = db.Column(db.String(20), db.ForeignKey('chatroom.room_name'))

    def __init__(self, message, userfrom, created_date, room_name="None"):
        self.message = message
        self.userfrom = userfrom
        self.created_date = created_date
        self.room_name = room_name

    def update(self: ChatLog, interface: ChatLogInterface) -> ChatLog:
        """Update to an existing room with a ChatLogInterface

        Parameters
        ----------
        interface: ChatLogInterface
            The log interface containing the changes to be implemented.

        Returns:
            ChatLog: The log with the updated changes.
        """

        for key, val in interface.items():
            setattr(self, key, val)
        return self
