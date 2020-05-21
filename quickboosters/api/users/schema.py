from __future__ import absolute_import

from marshmallow import Schema
from marshmallow import fields


class UserSchema(Schema):
    """A schema for users."""

    user_id = fields.Integer(attribute="user_id")
    username = fields.String(attribute="username")
    email = fields.String(attribute="email")
    role = fields.String(attribute="role")