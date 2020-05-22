from __future__ import annotations

from quickboosters import db
from quickboosters.api.roles.model import Role


def create_role():
    """Creates roles in the database"""

    admin_role = Role(name="Admin")
    db.session.add(admin_role)
    db.session.commit()
