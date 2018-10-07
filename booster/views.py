from flask import Flask, Blueprint, request
from flask_login import current_user

boosterbp = Blueprint('boosterbp', __name__, template_folder='templates/booster/templates/', static_folder='static')