from quickboosters.api.orders.model import Orders
from quickboosters.api.orders.enums import StatusEnum
from quickboosters.api.orders.enums import TypeEnum

import datetime
from quickboosters import db


def create_order():
    order = Orders(order_type=TypeEnum.solo_boost,
                   user_id='1',
                   order_amount=69.42,
                   status=StatusEnum.not_started,
                   date_ordered=datetime.datetime.now(),
                   game='league of legends')
    db.session.add(order)
    db.session.commit()
