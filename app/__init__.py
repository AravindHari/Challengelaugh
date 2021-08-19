from flask import Flask
from flask_socketio import SocketIO
import config
from flask_mongoengine import MongoEngine
from app.game.events import socketio
from app.game import game
from app.home import home


def create_app(test_config: dict=None)->Flask:
    app=Flask(__name__,static_folder=None)
    app.config.from_object(config)
    db=MongoEngine()
    db.init_app(app)
    app.register_blueprint(home,url_prefix='')
    app.register_blueprint(game,url_prefix='/game')
    socketio.init_app(app)
    return app
