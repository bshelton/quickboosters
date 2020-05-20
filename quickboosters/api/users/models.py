from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime
from quickboosters import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.String(80))

    def __init__(self, username, email, password, role="None"):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

 class UserRole(db.Model):
    __tablename__ = 'UserRole'
    id = int(users.id)
    user_id = (users.username)
    role_id = (role.roles)
    def __init__(self, id, user_id, role_id)
        self.id = id
        self.user_id = user_id
        self.role_id = role_id