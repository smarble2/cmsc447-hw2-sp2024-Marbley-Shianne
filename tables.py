#Author: Shianne Marbley
#Description: This will have flask 
#this file imports the sqlite3 connect aka my 
# database.db file and creates the initial state of the table of infos

import sqlite3

connected = sqlite3.connect('database.db') #connects to database.db file
print("database.db connected successfully") #print statemnet for confirm

connected.execute('CREATE TABLE info (name TEXT, id TEXT, points TEXT)')
#connected.execute('DROP TABLE info') 
print("Table created successfully")#print statemnet for confirm

connected.close() #close connection
print("Session closed successfully")
