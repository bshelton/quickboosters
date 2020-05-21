from __future__ import annotations

from flask import jsonify, request, Blueprint
import datetime
import jwt

from quickboosters.api.users.model import User
from quickboosters.api.users.interface import UserInterface
from quickboosters.api.users.schema import UserSchema
from quickboosters.api.users.service import UserService
from quickboosters.config import Config

auth = Blueprint('auth', __name__)


def _encodeAuthToken(user_id: User) -> jwt:
    now: datetime = datetime.datetime.now()
    payload = {
        'expiration': now + datetime.timedelta(days=0, seconds=60),
        'iat': now,
        'sub': user_id
    }
    token: jwt = jwt.encode(payload, Config().JWT_SECRET, algorithm='HS256')
    return token


def _validate_password(user_id: int, password: str) -> bool:

    if UserService().get_by_id(user_id).password == password:
        return True
    else:
        return False


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
        if user and _validate_password(user.id, password):
            token = _encodeAuthToken(user.id)
        return jsonify({
            'status': 'Success',
            'auth_token': token
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
        user_interface: UserInterface = UserSchema().load(request.get_json(force=True))
        return UserSchema.dumps(UserService.create(user_interface))
    except Exception as e:
        return jsonify({
            'status': 'failure',
            'error': e
        })

