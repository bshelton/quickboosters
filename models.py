from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

import datetime
from quickboosters import db


'''class Booster_Attributes(db.Model):
    balance = db.Column(db.Float)
    current_order = db.Column(db.Integer, db.ForeignKey('orders.id'))
    booster_id = db.Column(db.Integer)

    def __init__(self, booster_id, current_order=0, balance=0):
        self.booster_id = booster_id
        self.currender_order = current_order
        self.balance = balance
  '''      
