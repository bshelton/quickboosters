from quickboosters.api.order import order
from quickboosters.api.order.models import Orders

from flask import jsonify

@order.route('/order/<int:id>', methods=['GET'])
def get_order_by_id(id):
    
