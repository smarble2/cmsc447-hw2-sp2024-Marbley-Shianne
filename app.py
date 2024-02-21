#HUGE NOTE FOR MAC USERS YOU WILL GET A 403 ERROR WHEN YOU
#RUN THIS SCRIPT IN ORDER TO VIEW TURN OFF YOUR airplay reciever and reload the page
from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

#renders home page 

@app.route("/")
def homePage():
    #calls my homepage.html file
    return render_template("homepage.html")

@app.route('/form',methods=['GET', 'POST'])
def form():
    #This gets the data from the user input 
    if request.method == 'POST':
        name = request.form.get('name')
        ID = request.form.get('ID')
        points = request.form.get('Points')
    # Using submit button to insert the info into the datbase
        with sqlite3.connect("database.db") as user:
            cur = user.cursor()