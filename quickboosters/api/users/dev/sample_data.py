from quickboosters.api.users.models import User
from quickboosters import db
from quickboosters.api.order.models import Orders


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






