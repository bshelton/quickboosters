from __future__ import annotations
from __future__ import absolute_import

from typing import TypedDict
from datetime import datetime


class ChatRoomInterface(TypedDict, total=False):

    room_id: int
    room_name: str


class ChatLogInterface(TypedDict, total=False):

    log_id: int
    message: str
    userfrom: str
    created_date: datetime.now()
    room_name: str
