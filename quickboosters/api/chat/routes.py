from flask_socketio import SocketIO
from quickboosters.api.chat.models import ChatLog

app = Flask(__name__)
socketio = SocketIO(app)

#??????????@app.route('/chatlog')
#def sessions():
   # return 

def messageReceived(methods=['GET', 'POST']):
    print('message was received!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
