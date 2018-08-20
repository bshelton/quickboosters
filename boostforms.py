from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email, Length

leagues = ['Bronze 5', 'Bronze 4', 'Bronze 3', 'Bronze 2', 'Bronze 1']
silver = ['Silver 5', 'Silver 4', 'Silver 3', 'Silver 2', 'Silver 1']
gold = ['Gold 5', 'Gold 4', 'Gold 3', 'Gold 2', 'Gold 1']
zipped = zip(leagues, silver, gold)

print (zipped)
#Need a list of tuples


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


class SoloOrderForm(FlaskForm):
    current_rank = SelectField(label='Current Rank', choices=zipped)
