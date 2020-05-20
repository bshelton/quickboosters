from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from quickboosters.api.users.models import User
from quickboosters.api.chat import models, ChatLog

import datetime
from quickboosters import db


def Chatlog():
    Chatlog = ChatLog(message='message',userfrom='user.username',created_date=datetime.datetime.now())
    print(ChatLog)
    db.session.add(Chatlog)
    db.session.commit()