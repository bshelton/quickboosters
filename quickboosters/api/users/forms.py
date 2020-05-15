from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from quickboosters.api.users.models import User

class RegistrationForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Length(min=3, max=60), Email()])
    username = StringField(label='Username', validators=[DataRequired(), Length(min=1, max=30)])
    password = PasswordField(label='Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField(label='Confirm Password', validators=[DataRequired()])
    submit = SubmitField(label='Register Account')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email Already In Use')

class AccountDeactivation(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField(label='Confirm Password', validators=[DataRequired()])
    submit =SubmitField(label='Delete account')

