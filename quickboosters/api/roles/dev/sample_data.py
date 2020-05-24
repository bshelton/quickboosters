from __future__ import annotations

from quickboosters import db
from quickboosters.api.roles.model import Role


def create_role():
    """Creates roles in the database"""

    admin_role = Role(name="Admin")
    try:
        db.session.add(admin_role)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

        print(e)
