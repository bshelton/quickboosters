from __future__ import annotations

from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from quickboosters.api.users.auth import auth
from quickboosters.api.users.auth import login_required
from quickboosters.api.users.auth import encodeAuthToken
from quickboosters.api.users.auth import decodeAuthToken
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

@auth.route('/auth/checktoken', methods=["POST"])
def check():
    data = request.get_json()
    print(decodeAuthToken(data['auth_token']))
    return "token test"


@auth.route('/auth/needtoken', methods=["POST"])
@login_required
def need_token():
    return "You made it!"
