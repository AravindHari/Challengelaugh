from flask import Blueprint,render_template
from socketio.exceptions import SocketIOError


game=Blueprint('game',__name__,template_folder="templates",static_folder="static")

@game.route('/game')
def home():
    return "Home"





