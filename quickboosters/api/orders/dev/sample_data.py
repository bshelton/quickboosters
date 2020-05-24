from quickboosters.api.orders.model import Order
from quickboosters.api.orders.enums import StatusEnum
from quickboosters.api.orders.enums import TypeEnum
from quickboosters.api.games.enums import GameEnum

import datetime
from quickboosters import db


def create_order():
    order = Order(order_type=TypeEnum.solo_boost,
                   user_id='1',
                   order_amount=69.42,
                   status=StatusEnum.not_started,
                   date_ordered=datetime.datetime.now(),
                   game=GameEnum.league_of_legends)
    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
