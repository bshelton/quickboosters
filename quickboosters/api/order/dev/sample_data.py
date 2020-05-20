from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from quickboosters.api.users.models import User
from enum import Enum
from quickboosters.api.order.dev import sample_data

import datetime
from quickboosters import db


def create_order():
  order = Orders(order_type="solo_boost",user_id='1',order_amount=69.42,status='completed',date_ordered=datetime.datetime.now(),game='league of legends')
  print(order.user_id)
  db.session.add(order)
  db.session.commit()

#def order_status():
  #Orders(order_type="solo_boost", user_id='1', order_amount=69.42, status=Order_Status.in_process, created_date=datetime.datetime.now())
 # db.session.add(status)
  #db.session.commit()