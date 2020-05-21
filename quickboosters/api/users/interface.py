from __future__ import annotations
from __future__ import absolute_import
from datetime import datetime
from typing import TypedDict

from quickboosters.api.roles.model import RoleTypes


class UserInterface(TypedDict, total=False):
    """Defines types that make a user."""

    user_id: int
    username: str
    email: str
    password: str
    role: RoleTypes
    created_on: datetime
