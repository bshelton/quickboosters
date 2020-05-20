from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from quickboosters.api.users.models import User
from quickboosters.api.chat import models, ChatLog

import datetime
from quickboosters import db


def create_log():
    log = ChatLog(message='message',userfrom='Derek',created_date=datetime.datetime.now(),room='bronze')
    print(log)
    db.session.add(log)
    db.session.commit()