from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from quickboosters.api.order.models import Orders

import datetime
from quickboosters import db


def create_order():
  order = Orders(order_type="solo_boost",user_id='1',order_amount=69.42,status='completed',date_ordered=datetime.datetime.now(),game='league of legends')
  print(order.user_id)
  db.session.add(order)
  db.session.commit()