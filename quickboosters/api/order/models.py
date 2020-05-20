from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from enum import Enum
from quickboosters.api.order.dev import sample_data

import datetime
from quickboosters import db

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    order_type = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_amount = db.Column(db.Float, nullable=False)
    # booster_assigned = db.Column(db.String(20), db.ForeignKey('users.username'))
    date_ordered = db.Column(db.Date(), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    game = db.Column(db.String(30), nullable=False)

    
    def __init__(self,order_type, user_id, order_amount, status, date_ordered, game):
        self.order_type = order_type
        self.user_id = user_id
        self.order_amount = order_amount
        self.game = game
        self.status = status
        self.date_ordered = date_ordered

class Orders_Attributes(db.Model):
    __tablename__ = 'order_attributes'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    game_username = db.Column(db.String(30))
    game_password = db.Column(db.String(40))
    game_region = db.Column(db.String(30))

    def __init__(self,game_username, game_password, game_region, order_id):
        self.order_id = order_id
        self.game_username = game_username
        self.game_password = game_password
        self.game_region = game_region

class Order_Status(Enum):
    not_started = 1
    in_progress = 2
    complete = 3
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    game = db.Column(db.String(30), nullable=False)