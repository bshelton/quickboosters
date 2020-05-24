from __future__ import annotations
from __future__ import absolute_import
from datetime import datetime
from typing import TypedDict

from quickboosters.api.orders.enums import StatusEnum
from quickboosters.api.orders.enums import TypeEnum
from quickboosters.api.games.enums import GameEnum


class OrderInterface(TypedDict, total=False):

    order_id: int
    order_type: int
    user_id: int
    order_amount: float
    status: int
    game: int
    date_ordered: datetime
