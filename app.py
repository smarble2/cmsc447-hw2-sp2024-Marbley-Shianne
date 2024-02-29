#Author: Shianne Marbley
#Description: Flask app that controls the functionality of the app

#HUGE NOTE FOR MAC USERS YOU WILL GET A 403 ERROR WHEN YOU
#RUN THIS SCRIPT IN ORDER TO VIEW TURN OFF YOUR airplay reciever and reload the page
from flask import Flask
from flask import render_template
from flask import request, redirect,url_for
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
            cur.execute('INSERT INTO info (name,ID,Points) VALUES (?,?,?)',(name,ID,Points))
            user.commit()
         #data is inputted so it should be on the datatable   
        return redirect((url_for('datatable')))
    else:
        #otherwise reload the form page
        return render_template("form.html")
    
#view the entire datatable
@app.route('/datatable')
def datatable():
    #access rows inside the table
    connected = sqlite3.connect('database.db')
    connected.row_factory = sqlite3.Row

    cur = connected.cursor()
    #select * shows all data from info
    #rowid is a predefined thing by sqlite3 
    cur.execute('SELECT rowid,* FROM info')

    data = cur.fetchall()
    connected.close()
    #send results of the SELECT to the datatable.html
    return render_template("datatable.html", data = data) #used in datatables.html for loop user in data 

#Route will use the specific row then load edit form
@app.route("/edit", methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        try:
            #use hidden id from d[0] == rowid
            id = request.form['id']
            connected = sqlite3.connect("database.db")
            connected.row_factory = sqlite3.Row

            cur = connected.cursor()
            cur.execute("SELECT rowid, * FROM info WHERE rowid = " + id)

            data = cur.fetchall()
        except:
            id=None
        finally:
            #send row to edit form
            return render_template("edit.html",data = data) #data from the SELECT 
        
#update to actuallky update the datatable
@app.route("/editInfo",methods=['POST','GET']) 
def editInfo():
    # data will be from the post submitted by the form
    if request.method == 'POST':
        try:
            rowid = request.form['rowid'] 
            name = request.form['name']
            ID = request.form['ID']
            Points = request.form['Points']

            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("UPDATE info SET name='"+name+"', ID ='"+ID+"', Points='"+Points+"' WHERE rowid ="+rowid)

                conn.commit()
        except:
            conn.rollback()
        finally:
            return render_template('homepage.html')

    
if __name__ == '__main__':
    app.run(debug=False)