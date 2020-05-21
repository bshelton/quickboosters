from __future__ import annotations
from __future__ import absolute_import
from datetime import datetime
from typing import TypedDict

from quickboosters.api.order.model import Orders


class OrdersInterface(TypedDict, total=False):

    id: int
    order_type: str
    user_id: int
    order_amount: float
    #booster_assigned str
    status: str
    game: str
    date_ordered: datetime
   