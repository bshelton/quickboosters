from __future__ import annotations
from __future__ import absolute_import
from datetime import datetime
from typing import TypedDict


class OrdersInterface(TypedDict, total=False):

    id: int
    order_type: str
    user_id: int
    order_amount: float
    status: str
    game: str
    date_ordered: datetime
