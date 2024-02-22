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

#this commits the inputted data then either goes back to the
#homepage or if it doesn't work stays on the form page
@app.route('/form',methods=['GET', 'POST'])
def form():
    #this gets the data from the user input 
    if request.method == 'POST':
        name = request.form['name']
        ID = request.form['ID']
        Points = request.form['Points']
    #using submit button to insert the info into the datbase
        with sqlite3.connect("database.db") as user:
            cur = user.cursor()
            cur.execute("INSERT INTO info \
            (name,ID,Points) VALUES (?,?,?)",
                            (name,ID,Points))
            user.commit()
        return render_template("homepage.html")
    else:
        return render_template("form.html")

@app.route('/datatable')
def datatable():
    connected = sqlite3.connect('database.db')
    cur = connected.cursor()
    #select * shows all data from info 
    cur.execute('SELECT * FROM info')

    data = cur.fetchall()
    return render_template("datatable.html", data = data)
    
if __name__ == '__main__':
    app.run(debug=False)