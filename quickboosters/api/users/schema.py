from __future__ import absolute_import

from marshmallow import Schema
from marshmallow import fields


class UserSchema(Schema):
    """A schema for users."""

    user_id = fields.Integer(attribute="user_id")
    username = fields.String(attribute="username")
    password = fields.String(attribute="password")
    email = fields.String(attribute="email")
    role = fields.String(attribute="role")
    created_on = fields.DateTime()


summary_schema = UserSchema(only=("username", "email", "role"))
