from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy, functools
from sqlalchemy import func
from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, BooleanField
from passlib.hash import sha256_crypt
from forms import boostforms
from collections import OrderedDict
from flask_socketio import send, emit, join_room
import datetime

from quickboosters import app, db, socketio

mainbp = Blueprint('mainbp', __name__, template_folder='templates', static_folder='static')

@mainbp.route('/')
def index():
    return render_template('index.html')


@mainbp.route('/members')
@login_required
def memberdashboard():
    return render_template('members.html', name=current_user.username)

@mainbp.route('/admindashboard')
@login_required
def admindashboard():
    return render_template('admindashboard.html', name=current_user.username)

def determine_soloOrder_pricing():

    ranks = { 1 : 'Bronze 5', 2 : 'Bronze 4', 3 : 'Bronze 3', 4 : 'Bronze 2', 5 : 'Bronze 1',
     6 : 'Silver 5', 7 : 'Silver 4', 8 : 'Silver 3', 9 : 'Silver 2', 10 : 'Silver 1',
     11 : 'Gold 5', 12 : 'Gold 4', 13 : 'Gold 3', 14 : 'Gold 2', 15 : 'Gold 1',
     16 : 'Platinum 5', 17 : 'Platinum 4', 18 : 'Platinum 3', 19 : 'Platinum 2', 20 : 'Platinum 1',
     21 : 'Diamond 5', 22 : 'Diamond 4', 23 : 'Diamond 3', 24 : 'Diamond 2' , 25 : 'Diamond 1',
     26 : 'Master', 27 : 'Challenger'}

    one_league = 5
