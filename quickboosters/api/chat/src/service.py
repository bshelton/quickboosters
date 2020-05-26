from typing import List

from quickboosters.api.chat.model import ChatLog
from quickboosters.api.chat.interface import ChatLogInterface
from quickboosters.api.chat.interface import ChatRoomInterface
from quickboosters.api.chat.model import ChatRoom

from quickboosters import db


class ChatLogService:
    """Service for dealing with a ChatLog."""

    @staticmethod
    def get_all() -> List[ChatLog]:
        """Retrieve all logs.

        Returns:
        List[ChatLog]: a list of logs.
        """
        return ChatLog.query.all()

    @staticmethod
    def get_by_id(log_id: int) -> ChatLog:
        """Retrieve one log matching a given id.

        Returns:
            ChatLog: one log with id given
        """

        return ChatRoom.query.get(log_id)

    @staticmethod
    def create(attributes: ChatLogInterface) -> ChatLog:
        """ Creates a new log.

        Parameters
        ----------
        attributes: ChatLogInterface
            The attributes of a log
        Returns:
            ChatLog: The newly created log.
        """
        new_log: ChatLog = ChatLog(
            message=attributes["message"],
            userfrom=attributes["userfrom"],
            created_date=attributes["created_data"],
            room_name=attributes["room_name"]
        )
        db.session.add(new_log)
        db.session.commit()
        return new_log

    @staticmethod
    def update(log: ChatLog, changes: ChatLogInterface) -> ChatLog:
        """Update to an existing log with a ChatLogInterface

        Parameters
        ----------
        log: ChatLog
            The log to update.
        changes: ChatLogInterface
            The updates to the log.

        Returns:
            ChatLog: The log with the updated changes.
        """
        log.update(changes)
        db.session.commit()
        return log

    @staticmethod
    def delete_by_id(log_id: int) -> ChatLog:
        """Deletes a single log by id

        Parameters
        ----------
        log_id: int
            The room to delete

        Returns:
            ChatRoom: The room that was deleted
        """

        log: ChatLog = ChatLog.query.filter(ChatLog.log_id == log_id).first()
        db.session.delete(log)
        db.session.commit()
        return log


class ChatRoomService:
    """Service for dealing with a ChatRoom."""

    @staticmethod
    def get_all() -> List[ChatRoom]:
        """Retrieve all rooms.

        Returns:
        List[ChatRoom]: a list of rooms.
        """
        return ChatRoom.query.all()

    @staticmethod
    def get_by_id(room_id: int) -> ChatRoom:
        """Retrieve one room matching a given id.

        Returns:
            ChatRoom: one room with id given
        """

        return ChatRoom.query.get(room_id)

    @staticmethod
    def create(attributes: ChatRoomInterface) -> ChatRoom:
        """ Creates a new room.

        Parameters
        ----------
        attributes: ChatRoomInterface
            The attributes of an room
        Returns:
            ChatRoom: The newly created room.
        """
        new_room: ChatRoom = ChatRoom(
            room_name=attributes["room_name"]
        )
        db.session.add(new_room)
        db.session.commit()
        return new_room

    @staticmethod
    def update(room: ChatRoom, changes: ChatRoomInterface) -> ChatRoom:
        """Update to an existing room with a ChatRoomInterface

        Parameters
        ----------
        ChatRoom: ChatRoom
            The room to update.
        changes: ChatRoomInterface
            The updates to the room.

        Returns:
            ChatRoom: The room with the updated changes.
        """
        room.update(changes)
        db.session.commit()
        return room

    @staticmethod
    def delete_by_id(room_id: int) -> ChatRoom:
        """Deletes a single room by id

        Parameters
        ----------
        room_id: int
            The room to delete

        Returns:
            ChatRoom: The room that was deleted
        """

        room: ChatRoom = ChatRoom.query.filter(ChatRoom.room_id == room_id).first()
        db.session.delete(room)
        db.session.commit()
        return room
