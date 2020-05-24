from __future__ import annotations
from datetime import datetime

from quickboosters.api.games.enums import GameEnum
from quickboosters.api.orders.enums import TypeEnum, StatusEnum
from quickboosters.api.orders.model import Order
from quickboosters.api.orders.interface import OrderInterface
from quickboosters.api.orders.service import OrderService

from quickboosters.conftest import app


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


def test_create_order(app) -> None:
    with app.app_context():
        test_order = create_order()
        order: Order = OrderService().create(test_order)

        assert order.user_id == test_order.order_id
