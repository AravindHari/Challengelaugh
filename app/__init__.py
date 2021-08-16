from flask import Flask
from flask_socketio import SocketIO
import config
from app.game import socketio
from app.home import home


def create_app(test_config: dict=None)->Flask:
    app=Flask(__name__,static_folder=None)
    app.config.from_object(config)
    app.register_blueprint(home,url_prefix='')
    socketio.init_app(app)
    return app
