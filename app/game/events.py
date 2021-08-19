from app.home import data
from flask_socketio import SocketIO

socketio=SocketIO()


#Events
@socketio.on('connect')
def test_connect():
    print("SOCKET CONNECTED")

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))
    data.append(json)



