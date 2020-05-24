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
from quickboosters.api.users.interface import UserInterface
from quickboosters.api.users.service import UserService
from quickboosters.api.roles.enums import RoleTypes


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


def create_user() -> None:
    """ Nessecary for ForeignKey Constraint"""
    user: UserInterface = {
        "user_id": 1,
        "username": "exampleName",
        "email": "example@example.com",
        "password": "password",
        "role": RoleTypes.MEMBER,
        "created_on": datetime.now()
    }

    UserService().create(user)


def test_create_order(db: SQLAlchemy) -> None:
    create_user()
    test_order = create_order()
    order: Order = OrderService().create(test_order)
    assert order.user_id == test_order['user_id']


def test_get_all_orders(db: SQLAlchemy) -> None:
    create_user()
    test_order = create_order()
    OrderService().create(test_order)
    all_orders = OrderService().get_all()

    assert len(all_orders) > 0


def test_delete_order(db: SQLAlchemy) -> None:
    create_user()
    test_order = create_order()
    order: Order = OrderService().create(test_order)
    deleted_order: Order = OrderService.delete_by_id(order.order_id)
    assert deleted_order.order_id == order.order_id


def test_update_order(db: SQLAlchemy) -> None:
    create_user()
    test_order: OrderInterface = create_order()
    order: Order = OrderService().create(test_order)

    test_order['order_amount'] = 20.20
    updated_order: Order = OrderService().update(order, test_order)

    assert updated_order.order_amount == 20.20
