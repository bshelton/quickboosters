from quickboosters.backend.users.models import User
from quickboosters import db

from passlib.hash import sha256_crypt

def create_user():
    hashed_pw = sha256_crypt.hash("password")
    print(hashed_pw)
    user = User(username="brock", email="brock@brock.com", password=hashed_pw, role="Admin")
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(str(e))