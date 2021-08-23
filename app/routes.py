from flask import render_template,request
import random
import pickle
import sys
from app import app
data=[]

@app.route('/',methods=['POST','GET'])
def sign_in():
    if request.method=='POST':
        pass
    return render_template('signin.html')


@app.route('/home')
def end():
    print("SERVER STARTED")
    links=["https://www.youtube.com/embed/o28RANhwb0s","https://www.youtube.com/embed/IxG3Cv5qK00","https://www.youtube.com/embed/EtH9Yllzjcc"]
    a=1
    return render_template('index.html',url=links[a])


@app.route('/end')
def home_():
    print("SERVER END SAVING DATA")
    d=open('recogdata.pkl','wb')
    pickle.dump(data,d)
    return "Saved Successfully"





