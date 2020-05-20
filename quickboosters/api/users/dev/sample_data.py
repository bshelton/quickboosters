from quickboosters.api.users.models import User
from quickboosters import db
from quickboosters.api.order.models import Orders
from quickboosters.api.chat.models import ChatLog

from passlib.hash import sha256_crypt
import datetime

def create_user():
    hashed_pw = sha256_crypt.hash("password")
    print(hashed_pw)
    derek = User(username="derek", email="derek@brock.com", password=hashed_pw, role="Admin")
    try:
        db.session.add(derek)
        db.session.commit()
    except Exception as e:
        print(str(e))

def create_order():
  order = Orders(order_type="solo_boost",user_id='1',order_amount=69.42,status='completed',date_ordered=datetime.datetime.now(),game='league of legends')
  print(order.user_id)
  db.session.add(order)
  db.session.commit()

def Chatlog():
    Chatlog = ChatLog(message='message',userfrom='user.username',created_date=datetime.datetime.now())
    print(ChatLog)
    db.session.add(Chatlog)
    db.session.commit()

def order_status():
    status = Order_Status('status': order_status.enum, 'order_id': order_status.id, 'game': order_status.game)
    print(status)
    db.session.add(status)
    db.session.commit()





