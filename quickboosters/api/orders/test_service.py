from __future__ import annotations
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from quickboosters.tests.fixtures import app
from quickboosters.tests.fixtures import db

from quickboosters.api.games.enums import GameEnum
from quickboosters.api.orders.enums import TypeEnum, StatusEnum
from quickboosters.api.orders.model import Order
from quickboosters.api.orders.interface import OrderInterface
from quickboosters.api.orders.service import OrderService


def create_order() -> OrderInterface:
    order: OrderInterface = {
        "order_id": 1,
        "order_type": TypeEnum.solo_boost,
        "user_id": 1,
        "order_amount": 69.42,
        "status": StatusEnum.not_started,
        "game": GameEnum.league_of_legends,
        "date_ordered": datetime.now()
    }
    return order


def test_create_order(db: SQLAlchemy) -> None:
    test_order = create_order()
    order: Order = OrderService().create(test_order)
    assert order.user_id == test_order['user_id']
