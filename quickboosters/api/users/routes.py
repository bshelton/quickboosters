#add and delete users
from flask import render_template
from quickboosters.api.users import auth
from quickboosters.api.users.forms import RegistrationForm
from quickboosters.api.users.models import User
from passlib.hash import sha256_crypt
from quickboosters import db

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)

    return render_template("register.html", form=form)