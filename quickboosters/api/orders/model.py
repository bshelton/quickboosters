from __future__ import annotations
from enum import Enum
import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from quickboosters import db
from quickboosters.api.games.enums import GameEnum


class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    order_type = Column(Enum(TypeEnum), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    order_amount = Column(Float(), nullable=False)
    date_ordered = Column(DateTime(), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)
    game = Column(Enum(GameEnum), nullable=False)
  
    def __init__(self, order_type, user_id, order_amount, status, date_ordered, game):
        self.order_type = order_type
        self.user_id = user_id
        self.order_amount = order_amount
        self.game = game
        self.status = status
        self.date_ordered = date_ordered


class StatusEnum(Enum):
    not_started = 1
    in_progress = 2
    complete = 3


class TypeEnum(Enum):
    solo_boost = 1
    duo_boost = 2