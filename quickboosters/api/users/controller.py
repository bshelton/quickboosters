from __future__ import annotations

from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from quickboosters.api.users.auth import auth
from quickboosters.api.users.helper import send_password_reset_email
from quickboosters.api.users.auth import login_required
from quickboosters.api.users.auth import encodeAuthToken
from quickboosters.api.users.auth import decodeAuthToken
from quickboosters.api.users.model import User
from quickboosters.api.users.schema import UserSchema
from quickboosters.api.users.service import UserService


@auth.route('/auth/login', methods=['POST'])
def login_and_generate_token() -> str:
    """API route to generate token.

    Returns the new token

    Returns:
        str: a JSON encoded response.
    """

    req_json: dict = request.get_json()

    username: str = req_json['username']
    password: str = req_json['password']
    user = UserService().get_by_username(username)

    try:
        if user and user.check_password(password):
            token = encodeAuthToken(user.id)
        return jsonify({
            'status': 'Success',
            'auth_token': token.decode('UTF-8')
        })
    except Exception as e:
        return jsonify({
            'status': 'failure',
            'error': e
        })


@auth.route('/auth/register', methods=['POST'])
def register_user():
    """An API route to create a new user.

    Returns the new created user.

    Returns:
        str: A JSON encoded response.
    """

    try:
        schema = UserSchema()
        new_user = UserService().create(schema.load(request.get_json()))
        return {
            "user": new_user.username
        }
    except IntegrityError:
        return jsonify({
            'status': 'failure',
            'error': request.get_json()['username'] + ' already taken.'
        })
    except Exception as e:
        return jsonify({
            'status': 'failure',
            'error': e
        })


@auth.route('/password-reset', methods=['POST'])
def reset_password_request():
    data = request.get_json()
    email = data['email']
    user = UserService().get_by_email(email)
    if user:
        print("asdas")
        send_password_reset_email(user)
    return "sent email"

@auth.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    user = User.verify_reset_password_token(token)

    if user:
        UserService().update(user.id)