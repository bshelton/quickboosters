from flask import Blueprint
auth = Blueprint('auth', __name__)
from quickboosters.api.users import routes
