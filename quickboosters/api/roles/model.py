from enum import Enum

from quickboosters import db

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Role(db.Model):
    __tablename__ = 'roles'
    role_id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True)

    def __init__(self, name):
        self.name = name


class UserToRole(db.Model):
    __tablename__ = 'user_to_role'
    user_to_role_id = Column(Integer(), primary_key=True)
    role_id = Column(Integer(), ForeignKey('roles.role_id'))
    user_id = Column(Integer(), ForeignKey('users.user_id'))


class RoleTypes(Enum):
    MEMBER = 'Member'
    BOOSTER = 'Booster'
    ADMIN = 'Admin'
