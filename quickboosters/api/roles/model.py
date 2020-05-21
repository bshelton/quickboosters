from enum import Enum

from quickboosters import db

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Role(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True)
    usertorole = relationship("user_to_role")

    def __init__(self, name):
        self.name = name


class UsertoRole(db.Model):
    __tablename__ = 'user_to_role'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    role_id = Column(Integer(), ForeignKey('roles.id'), nullable=False)

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id


class RoleTypes(Enum):
    MEMBER = 1
    BOOSTER = 2
    ADMIN = 3
