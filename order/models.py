from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

import datetime
from quickboosters import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_type = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_amount = db.Column(db.Float, nullable=False)
    booster_assigned = db.Column(db.String(20), db.ForeignKey('users.username'))

    def __init__(order_type, user_id, order_amount, booster_assigned="None"):
        self.message = message
        self.userfrom = userfrom
        self.created_date = created_date
        self.booster_assigned = booster_assigned