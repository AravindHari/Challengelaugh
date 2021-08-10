from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import config

app=Flask(__name__)

app.config.from_object(config)


cors=CORS(app)

socketio=SocketIO(app)

from app import routes