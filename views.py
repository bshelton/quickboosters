from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy, functools
from sqlalchemy import func
from flask_wtf import FlaskForm

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
    return render_template('usercurrentorder.html', name=current_user.username)
