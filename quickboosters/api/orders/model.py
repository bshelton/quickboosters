from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from quickboosters import db
from quickboosters.api.orders.interface import OrderInterface
from quickboosters.api.orders.enums import TypeEnum
from quickboosters.api.orders.enums import StatusEnum
from quickboosters.api.games.enums import GameEnum


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = Column(Integer(), primary_key=True)
    order_type = Column(Enum(TypeEnum), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.user_id'), nullable=False)
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

    def update(self: Order, interface: OrderInterface) -> Order:
        """Update to an existing order with a OrderInterface

        Parameters
        ----------
        interface: OrderInterface
            The order interface containing the changes to be implemented.

        Returns:
            Order: The order with the updated changes.
        """

        for key, val in interface.items():
            setattr(self, key, val)
        return self
