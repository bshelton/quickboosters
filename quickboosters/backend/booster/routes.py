from quickboosters import db
from flask import Flask, Blueprint, request, render_template
from flask_login import current_user,login_required
from quickboosters.order.models import Orders
from quickboosters.users.models import User
from quickboosters.forms import boostforms
from passlib.hash import sha256_crypt

boosterbp = Blueprint('boosterbp', __name__, template_folder='templates', static_folder='static/boosters')

@boosterbp.route('/booster/dashboard')
@login_required
def booster_dashboard():

    return render_template('/boosters/index.html', username=current_user.username, user=current_user.username)

@boosterbp.route('/booster/getorder')
def booster_get_order():

    orders = Orders.query.filter(Orders.status!='In Progress').all()
    return render_template('/boosters/get_order.html', orders=orders)

@boosterbp.route('/booster/currentoders')
@login_required
def currentorders():

    orders = Orders.query.filter(Orders.booster_assigned==current_user.username).all()
    print(orders)

    return render_template('/boosters/current_orders.html', orders=orders)

@boosterbp.route('/booster/edit_profile', methods=['GET', 'POST'])
@login_required
def editprofile():

    profileForm = boostforms.BoosterUpdateInfoForm()

    if profileForm.validate_on_submit():

        submitted_email = profileForm.email.data
        password = profileForm.password.data
        hash_password = sha256_crypt.hash(profileForm.password.data)
        
        user = User.query.filter(User.username==current_user.username).first()

        if user.email != submitted_email and submitted_email != '':
            #new_user = User(username=profileForm.username.data, email=form.email.data, password=hash_password)
            user.email = submitted_email
            try:
                db.session.commit()
            finally: 
                return render_template('/boosters/edit_profile.html', username=current_user.username, user=current_user, profileForm=profileForm)

        if sha256_crypt.verify(password, user.password):

            print("Password submitted matches what's in the database, nothing to do.")
        else:
            user.password = hash_password

            try:
                db.session.commit()
            finally:
                return render_template('/boosters/edit_profile.html', username=current_user.username, user=current_user, profileForm=profileForm)

    return render_template('/boosters/edit_profile.html', username=current_user.username, user=current_user, profileForm=profileForm)