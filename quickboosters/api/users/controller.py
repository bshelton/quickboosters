from __future__ import annotations

from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from quickboosters.api.users.auth import auth
from quickboosters.api.users.helper import send_password_reset_email
from quickboosters.api.users.helper import send_email
from quickboosters.api.users.auth import encodeAuthToken
from quickboosters.api.users.model import User
from quickboosters.api.users.interface import UserInterface
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
            'error': str(e)
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
            'error': str(e)
        })


@auth.route('/password-reset', methods=['POST'])
def reset_password_request():
    """Sends an email with a JWT token"""

    url = request.host_url + 'password-reset/'

    data = request.get_json()
    email = data['email']
    user = UserService().get_by_email(email)
    try:
        if user:
            send_password_reset_email(user, url)

            return jsonify({
                'status': 'success',
                'message': 'Email sent to: ' + email
            })
    except Exception as e:
        return jsonify({
            'status': 'failure',
            'error': str(e)
        })


@auth.route('/password-reset/<token>', methods=['POST'])
def reset_password(token):
    """Resets a users password given a valid token.

    Parmaeters
    ----------
    token:
        The JWT that was sent to the users email.
    """
    data = request.get_json()

    user = User.verify_reset_password_token(token)
    updates = UserInterface()
    updates['password'] = data['new_password']
    try:
        if user:
            UserService().update(user, updates)

            send_email("[QuickBoosters] Password Reset",
                       "password reset successfully",
                       "noreply@quickboosters.com",
                       user.email)
            return jsonify({
                'status': 'success',
                'message': 'Password successfully updated'
            })
    except Exception as e:
        return jsonify({
            'status': 'failure',
            'message': str(e)
        })
