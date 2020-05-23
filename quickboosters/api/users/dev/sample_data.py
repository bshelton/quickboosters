from quickboosters.api.users.model import User
from quickboosters import db

from passlib.hash import sha256_crypt


def create_user():
    hashed_pw = sha256_crypt.hash("password")
    print(hashed_pw)
    derek = User(username="derek", email="derek@brock.com", password=hashed_pw, role="Admin")
    try:
        db.session.add(derek)
        db.session.commit()
    except Exception as e:
        print(str(e))
