from flask import Flask, render_template, Blueprint
from flask_login import login_required, login_url, current_user

from quickboosters import app, db, socketio

adminbp = Blueprint('adminbp', __name__, template_folder='templates/admin', static_folder='static/admin/static')

@adminbp.route('/admindashboard')
@login_required
def admindashboard():
    return render_template('admindashboard.html', name=current_user.username)