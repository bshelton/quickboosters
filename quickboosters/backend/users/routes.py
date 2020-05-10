from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy, functools
from flask_socketio import send, emit, join_room
from sqlalchemy import func, and_

from passlib.hash import sha256_crypt
import datetime

from quickboosters import db, socketio
from quickboosters.backend.forms import boostforms
from quickboosters.backend.users.models import User
from quickboosters.backend.order.models import Orders, Orders_Attributes

userbp = Blueprint('userbp', __name__, template_folder='templates', static_folder='static')

@userbp.route('/login', methods=['GET', 'POST'])
def login():
    form = boostforms.LoginForm()
    if form.validate_on_submit():
        submitted_username = form.username.data
        submitted_username = str(submitted_username)
        submitted_username = submitted_username.lower()

        user = User.query.filter(func.lower(User.username)==submitted_username).first()
        if user:
            if user.username.lower() == submitted_username.lower():
                if sha256_crypt.verify(form.password.data, user.password):
                    login_user(user, remember=form.remember.data)
                    return redirect(request.args.get('next') or url_for('userbp.userdashboard'))
                else:
                     return '<h1> Wrong Password: Will Change Later </h1>'
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


@userbp.route('/users/order/<id>', methods=['GET', 'POST'])
@login_required
def usercurrentorder(id):
    user = User.query.filter(User.username == current_user.username).first()
    order = Orders.query.filter(and_(Orders.id==id, Orders.user_id==user.id)).first()

    form = boostforms.LeagueSoloBoostForm()

    if form.validate_on_submit():
        game_username = form.game_username.data
        game_password = form.game_password.data
        game_region = form.game_region.data

        order_attrib = Orders_Attributes(game_username=game_username, game_password=game_password, game_region=game_region, order_id=id)
        db.session.add(order_attrib)
        db.session.commit()

    return render_template('usercurrentorder.html', name=current_user.username, order=order, form=form, id=id)

@userbp.route('/userdashboard')
@login_required
def userdashboard():
    user = User.query.filter(User.username == current_user.username).first()
    solo_orders = Orders.query.filter(and_(Orders.user_id==user.id, Orders.order_type=="Solo Boost")).all()

    duo_orders = Orders.query.filter(and_(Orders.user_id==user.id, Orders.order_type=="Duo Boost")).all()
    return render_template('userdashboard.html', name=current_user.username, duo_orders=duo_orders, solo_orders=solo_orders)