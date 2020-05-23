from smtplib import SMTP
from flask import render_template

from quickboosters import DevConfig
from quickboosters.api.users.model import User


server = SMTP(host=DevConfig.SMTP_SERVER,
              port=DevConfig.SMTP_PORT)

def send_email(subject, text, sender, recipient):
    message = 'Subject: {}\n\n{}'.format(subject, text)
    server.sendmail(sender, recipient, message)


def send_password_reset_email(user: User):
    token = user.get_reset_password_token()
    send_email('[QuickBoosers] Reset Your Password',
               sender='no-reply@quickboosters.com',
               recipient=[user.email],
               text=render_template('email/reset-password.txt',
                                         user=user, token=token))