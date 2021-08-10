from flask import redirect,render_template
from flask_socketio import emit,send
from app import app,socketio
import random
import pickle

data=[]

@app.route('/')
def end():
    print("SERVER STARTED")
    links=["https://www.youtube.com/embed/o28RANhwb0s","https://www.youtube.com/embed/IxG3Cv5qK00","https://www.youtube.com/embed/EtH9Yllzjcc"]
    a=random.randint(0,len(links))
    return render_template('index.html',url=links[a])


@app.route('/end')
def home():
    print("SERVER END SAVING DATA")
    d=open('recogdata.pkl','wb')
    pickle.dump(data,d)
    return "Saved Successfully"

    


@socketio.on('connect')
def test_connect():
    print("SOCKET CONNECTED")

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))
    data.append(json)
