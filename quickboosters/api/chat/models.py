from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


import datetime

from quickboosters import db
from quickboosters.api.users.models import User


class ChatRoom(db.Model):
    __tablename__ = 'chatroom'
    id = db.Column(db.Integer, primary_key=True)
    roomname = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, roomname):
        self.roomname = roomname

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)
    userfrom = db.Column(db.String(20), db.ForeignKey('users.username'), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True))
    room = db.Column(db.String(20), db.ForeignKey('chatroom.roomname'))

    def __init__(self, message, userfrom, created_date, room="None"):
        self.message = message
        self.userfrom = userfrom
        self.created_date = created_date
        self.room = room