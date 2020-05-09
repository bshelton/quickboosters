from quickboosters import db, socketio
from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import login_required, current_user
from quickboosters.chat.models import ChatLog, ChatRoom
from quickboosters.users.models import User
from quickboosters.order.models import Orders
from flask_socketio import send, emit, join_room
import datetime

chatbp = Blueprint('chatbp', __name__, template_folder='templates', static_folder='static')

users = {}

@chatbp.route('/chat')
@login_required
def usertobooster_chat():
    return render_template('usertobooster.html', name=current_user.username)

@socketio.on('message')
@login_required
def received_message(message):
    print (current_user.username + " Connected To Chat.")
    users[current_user.username] = request.sid
def message_received(methods=['GET', 'POST']):
    print ('message received')


@socketio.on('booster_msg', namespace='/booster')
@login_required
def handle_booster_msg(json, methods=['GET', 'POST']):
    print (str(json))
    roomname = 'Boosters_Chat'

    try:
        cr = ChatRoom(roomname=roomname)
        db.session.add(cr)
        db.session.commit()
    except:
        print ("Couldn't build Chatroom")
    finally:
        join_room(roomname)
        socketio.emit('display_to_booster_chat', json, room=roomname, callback=message_received, namespace='/booster')


@socketio.on('client_msg')
@login_required
def handle_client_msg(json, methods=['GET', 'POST']):
    print (str(json))

    #Get the user who sent the msg
    user = User.query.filter(User.username == current_user.username).first()
    
    #Check to see if user is a client
    if current_user.username == user.username and user.role == "client":
        booster = match_user_with_booster(user)
        
        #Create a room name
        roomname = str(current_user.username) + str(booster)
        cr = ChatRoom(roomname=roomname)

        try:
            db.session.add(cr)
            db.session.commit()
            
        finally:
            join_room(roomname)
            socketio.emit('display_to_chat', json, room=roomname, callback=message_received)

    elif user.role == "Booster": # Else was the user who sent the message a booster?
        user = match_booster_with_user(user)
        
        roomname = str(user) + str(current_user.username)
        roomtojoin = ChatRoom.query.filter(ChatRoom.roomname==roomname).first()
        print (roomtojoin)
        cr = ChatRoom(roomname=roomtojoin.roomname)

        print (roomtojoin.roomname)
        join_room(roomtojoin.roomname)
        socketio.emit('display_to_chat', json, room=roomname, callback=message_received)
    else:
        print (current_user.username)
        join_room(request.sid)

    try:
        msg = ChatLog(json['message'], current_user.username, datetime.datetime.now(), room=roomname)
    finally:
        db.session.add(msg)
        db.session.commit()
    
def handle_join_room(room):
    join_room(room)

#Returned a booster that is assigned to a user
def match_user_with_booster(user):
    print ("User sent MSG")
    order = Orders.query.filter(Orders.user_id==user.id).first()
    print ("booster assigned to order: " + order.booster_assigned)
    print ("SEnding to " + order.booster_assigned)
    return order.booster_assigned

#Returns a user that the booster is assigned to
def match_booster_with_user(booster):
    print ("Booster Sent MSG")
    order = Orders.query.filter(Orders.booster_assigned==booster.username).first()
    customer = User.query.filter(User.id==order.user_id).first()
    print ("Sending to " + customer.username)

    return customer.username