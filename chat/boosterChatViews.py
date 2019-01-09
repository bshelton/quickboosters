from quickboosters import app, db, socketio
from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import login_required, current_user
from chat.models import ChatLog, ChatRoom
from users.models import User
from order.models import Orders
from flask_socketio import send, emit, join_room
import datetime

users = {}

@socketio.on('booster_msg')
@login_required
def handle_booster_msg(json, methods=['GET', 'POST']):
    print (str(json))

