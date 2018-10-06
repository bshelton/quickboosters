from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy, functools
from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, BooleanField
from forms import boostforms

orderbp = Blueprint('orderbp', __name__, template_folder='templates', static_folder='static')


@orderbp.route('/order', methods=['GET', 'POST'])
def order():
    form = boostforms.SoloOrderForm()

    if form.validate_on_submit():
        current_league = form.current_league.data
        current_division = form.current_division.data
        current_lp = form.current_lp.data

        desired_league = form.desired_league.data
        desired_division = form.desired_division.data
        desired_lp = form.desired_lp.data

    return render_template('order.html', form=form)
