from __future__ import annotations
import functools
import datetime

from flask import Blueprint, Response, request, make_response
import jwt

from quickboosters.api.users.model import User

auth = Blueprint('auth', __name__)


def get_encoded_token() -> jwt:
    """Gets a JWT token from auth header.

    Return:
        The encoded JSON Web Token.
    """
    token: jwt = None

    if "authorization" in request.headers:
        token = request.headers["authorization"]
    elif "jwt" in request.cookies:
        token = request.cookies["jwt"]

    return token


def encodeAuthToken(user_id: User) -> jwt:
    now: datetime = datetime.datetime.now()

    payload = { 
        'exp': now + datetime.timedelta(days=0, minutes=300),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token


def decodeAuthToken(token: jwt) -> jwt:
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return {
            'status': 'failure',
            'message': 'expired token'
        }
    except jwt.InvalidTokenError:
        return {
            'status': 'failure',
            'message': 'invalid token'
        }


def login_required(func):
    """Make sure the user is logged in before proceeding"""

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        token = decodeAuthToken(get_encoded_token())
        print(token)
        if isinstance(token, int):
            return func(*args, **kwargs)

        if token['status'] == 'failure':
            msg = "Unauthorized Access, please login."
            return make_response(Response(msg, status=401, headers={'status': 'failure'}))
   
    return decorated
