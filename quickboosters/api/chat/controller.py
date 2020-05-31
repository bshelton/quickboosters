from flask import request, session, \
    copy_current_request_context, render_template
from quickboosters.api.chat import chat
from quickboosters import socketio
from flask_socketio import emit, join_room, leave_room, \
    rooms, disconnect, close_room


@chat.route('/chat', methods=["GET", "POST"])
def chat_test():
    return render_template('chat_test.html')


@socketio.on('my_event', namespace='/test')
def test_message(message):
    emit('my_response',
         {'data': message['data']})


@socketio.on('connect', namespace='/test')
def test_connect():
    print("Someone connected")
    # emit('my_response', {'data': 'Connected to chat', 'count': 0})
