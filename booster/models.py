from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

import datetime
from quickboosters import db



class Booster(UserMixin, db.Model):
    __tablename__ = 'boosters'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password