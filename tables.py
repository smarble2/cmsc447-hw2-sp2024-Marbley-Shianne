#Author: Shianne Marbley
#Description: This will have flask 
#this file imports the sqlite connect aka my 
# database.db file

import sqlite3

connected = sqlite3.connect('database.db') #connects to database.db file
print("database.db connected successfully") #print statemnet for confirm

connected.execute('CREATE TABLE info (name TEXT, id TEXT, points TEXT)')
#connected.execute('DROP TABLE info') 
print("Table created successfully")#print statemnet for confirm

connected.close() #close connection
