from datetime import datetime
from quickboosters.api.roles.model import RoleTypes
from quickboosters.api.users.model import User
from quickboosters import db

from passlib.hash import sha256_crypt


def create_user():
    hashed_pw = sha256_crypt.hash("password")
    print(hashed_pw)
    derek = User(username="derek",
                 email="derek@brock.com",
                 password=hashed_pw,
                 role="Admin",
                 created_on=datetime.now())
    try:
        db.session.add(derek)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(str(e))
