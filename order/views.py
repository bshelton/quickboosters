from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy, functools
from flask_wtf import FlaskForm

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

        price = determine_soloOrder_pricing(current_league, desired_league, current_division, desired_division)
        print (price)

    return render_template('order.html', form=form)

@orderbp.route('/purchase', methods=['GET', 'POST'])
def purchase():
    soloform = boostforms.SoloOrderForm()

    if soloform.validate_on_submit():
        current_league = form.current_league.data
        current_division = form.current_division.data
        current_lp = form.current_lp.data

        desired_league = form.desired_league.data
        desired_division = form.desired_division.data
        desired_lp = form.desired_lp.data

        price = determine_soloOrder_pricing(current_league, desired_league, current_division, desired_division)
        print (price)

    return render_template('purchase.html', soloform=soloform)

def determine_soloOrder_pricing(cl, dl, cd, dd):

    ranks = { 1 : 'Bronze 5', 2 : 'Bronze 4', 3 : 'Bronze 3', 4 : 'Bronze 2', 5 : 'Bronze 1',
     6 : 'Silver 5', 7 : 'Silver 4', 8 : 'Silver 3', 9 : 'Silver 2', 10 : 'Silver 1',
     11 : 'Gold 5', 12 : 'Gold 4', 13 : 'Gold 3', 14 : 'Gold 2', 15 : 'Gold 1',
     16 : 'Platinum 5', 17 : 'Platinum 4', 18 : 'Platinum 3', 19 : 'Platinum 2', 20 : 'Platinum 1',
     21 : 'Diamond 5', 22 : 'Diamond 4', 23 : 'Diamond 3', 24 : 'Diamond 2' , 25 : 'Diamond 1',
     26 : 'Master', 27 : 'Challenger'}

    one_league = 5

    current_rank = str(cl) + ' ' + str(cd)

    desired_rank = str(dl) + ' ' + str(dd)

    for rank, league in ranks.items():
        if desired_rank == league:
            desired_rank2 = rank
        if current_rank == league:
            current_rank2 = rank
  
    difference_rank = desired_rank2 - current_rank2
    
    return difference_rank * 5.0
