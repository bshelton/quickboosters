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
from users.models import User

userbp = Blueprint('userbp', __name__, template_folder='templates', static_folder='static')

@userbp.route('/login', methods=['GET', 'POST'])
def login():
    form = boostforms.LoginForm()
    if form.validate_on_submit():
        submitted_username = form.username.data
        submitted_username = str(submitted_username)
        submitted_username = submitted_username.lower()

        user = User.query.filter(func.lower(User.username)==submitted_username).first()
        print (user)
        if user:
            if user.username.lower() == submitted_username.lower():
                if sha256_crypt.verify(form.password.data, user.password) and user.role == "Admin":
                    login_user(user, remember=form.remember.data)
                    return redirect(request.args.get('next') or url_for('mainbp.admindashboard'))
                elif sha256_crypt.verify(form.password.data, user.password) and user.role == "Client":
                    login_user(user, remember=form.remember.data)
                    return redirect(request.args.get('next') or url_for('userbp.userdashboard'))
                elif sha256_crypt.verify(form.password.data, user.password) and user.role == "None":
                    login_user(user, remember=form.remember.data)
                    return redirect(request.args.get('next') or url_for('userbp.userdashboard'))
                else:
                     return '<h1> Wrong Password: Will Change Later </h1>'
            else:
                return '<h1> Invalid Login </h1>'
        else:
            return '<h1> Invalid Login </h1>'
    return render_template('login.html', form=form)


@userbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('mainbp.index'))

@userbp.route('/register', methods=['GET', 'POST'])
def register():
    form = boostforms.RegisterForm()

    if form.validate_on_submit():
        hash_password = sha256_crypt.hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('userbp.login'))

    return render_template('register.html', form=form)


@userbp.route('/userdashboard')
@login_required
def userdashboard():
    return render_template('members.html', name=current_user.username)