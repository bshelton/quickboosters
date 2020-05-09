from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy, functools
from flask_socketio import send, emit, join_room
from flask_wtf import FlaskForm
from sqlalchemy import func

from passlib.hash import sha256_crypt
from collections import OrderedDict
import datetime

from quickboosters.forms import boostforms
from quickboosters import db, socketio

mainbp = Blueprint('mainbp', __name__, template_folder='templates', static_folder='static')

@mainbp.route('/')
def index():
    return render_template('index.html')

@mainbp.route('/members')
def memberdashboard():
    return render_template('usercurrentorder.html', name=current_user.username)
