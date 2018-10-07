from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from users.models import User

import datetime
from quickboosters import db

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    order_type = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_amount = db.Column(db.Float, nullable=False)
    booster_assigned = db.Column(db.String(20), db.ForeignKey('users.username'))
    date_ordered = db.Column(db.Date(), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    game = db.Column(db.String(30), nullable=False)

    def __init__(order_type, user_id, order_amount, status, date_ordered, game, booster_assigned="None"):
        self.order_type = order_type
        self.user_id = user_id
        self.order_amount = order_amount
        self.game = game
        self.booster_assigned = booster_assigned
        self.status = status
        self.date_ordered = date_ordered

class Orders_Attributes(db.Model):
    __tablename__ = 'order_attributes'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    game_username = db.Column(db.String(30))
    game_password = db.Column(db.String(40))
    game_region = db.Column(db.String(30))

    def __init__(game_username, game_password, game_region):
        self.game_username = game_username
        self.game_password = game_password
        self.game_region = game_region

