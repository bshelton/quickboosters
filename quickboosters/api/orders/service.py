from typing import List

from quickboosters.api.orders.interface import OrderInterface
from quickboosters.api.orders.model import Order

from quickboosters import db

class OrderService:
    """Service for dealing with an Order."""

    @staticmethod
    def get_all() -> List[Order]:
        """Retrieve all users.

        Returns:
        List[User]: a list of users.
        """
        return Order.query.all()

    @staticmethod
    def get_by_id(order_id: int) -> Order:
        """Retrieve one order matching a given id.

        Returns:
            Order: one order with id given
        """

        return Order.query.get(order_id)

    @staticmethod
    def create(attributes: OrderInterface) -> Order:
        """ Creates a new order.

        Parameters
        ----------
        attributes: OrderInterface
            The attributes of an order
        Returns: 
            Order: The newly created order.
        """
        new_order: Order = Order(
            order_type=attributes["order_type"],
            user_id=attributes["user_id"],
            order_amount=attributes["order_amount"],
            status=attributes["status"],
            game=attributes["game"],
            date_ordered=attributes["date_ordered"])
        db.session.add(new_order)
        db.session.commit()
        return new_order
