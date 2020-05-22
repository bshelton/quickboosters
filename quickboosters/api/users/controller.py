from __future__ import annotations

from flask import jsonify, request, Blueprint
from sqlalchemy.exc import IntegrityError
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
        'exp': now + datetime.timedelta(days=0, seconds=5),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token


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
            token = _encodeAuthToken(user.id)
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
