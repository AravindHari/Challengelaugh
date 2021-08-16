from flask import Blueprint
from flask import render_template
import random
import pickle
import sys
data=[]
home=Blueprint('home',__name__,template_folder="templates",static_folder="static",static_url_path='static')

@home.route('/')
@home.route('/home')
def end():
    print("SERVER STARTED")
    links=["https://www.youtube.com/embed/o28RANhwb0s","https://www.youtube.com/embed/IxG3Cv5qK00","https://www.youtube.com/embed/EtH9Yllzjcc"]
    a=1
    return render_template('index.html',url=links[a])


@home.route('/end')
def home_():
    print("SERVER END SAVING DATA")
    d=open('recogdata.pkl','wb')
    pickle.dump(data,d)
    return "Saved Successfully"