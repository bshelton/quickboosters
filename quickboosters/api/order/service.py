from typing import List

from quickboosters.api.order.interface import OrdersInterface
from quickboosters.api.order.model import Orders

from quickboosters import db

class OrderService:
    """Service for dealing with Orders."""

    @staticmethod
    def get_all() -> List[Orders]:
        """Retrieve all users.

        Returns:
        List[User]: a list of users.
        """
        return Orders.query.all()

    @staticmethod
    def get_by_id(order_id: int) -> Orders:
        """Retrieve one order matching a given id.

        Returns:
            Order: one order with id given
        """

        return Orders.query.get(order_id)

    @staticmethod
    def create(attributes: OrdersInterface) -> Orders:
        """ Creates a new order.

        Parameters
        ----------
        attributes: OrderInterface
            The attributes of an order
        Returns: 
            Order: The newly created order.
        """
        orders: Orders = Orders(
            order_type=attributes["order_type"],
            user_id=attributes["user_id"],
            order_amount=attributes["order_amount"],
            status=attributes["status"],
            game=attributes["game"],
            date_ordered=attributes["date_ordered"])
        db.session.add(orders)
        db.session.commit()
        return orders

    