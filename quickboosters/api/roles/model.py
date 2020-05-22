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

    def __init__(self, name):
        self.name = name


class RoleTypes(Enum):
    MEMBER = 1
    BOOSTER = 2
    ADMIN = 3
