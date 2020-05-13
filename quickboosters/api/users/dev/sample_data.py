from quickboosters.api.users.models import User
from quickboosters import db

from passlib.hash import sha256_crypt

def create_user():
    hashed_pw = sha256_crypt.hash("password")
    print(hashed_pw)
    user = User(username="brock", email="brock@brock.com", password=hashed_pw, role="Admin")
    user2 = User(username="jonah", email="jonah@jonah", password=hashed_pw, role="Admin")
    try:
        #db.session.add(user)
        db.session.add(user2)
        db.session.commit()
    except Exception as e:
        print(str(e))