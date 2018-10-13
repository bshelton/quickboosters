from flask import Flask, Blueprint, request, render_template
from flask_login import current_user

boosterbp = Blueprint('boosterbp', __name__, template_folder='templates', static_folder='static/boosters')


@boosterbp.route('/booster/dashboard')
def booster_dashboard():

    return render_template('/boosters/index.html')