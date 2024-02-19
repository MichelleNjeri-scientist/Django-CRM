# Installed mysql on computer

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'M1sh@1vy'
    
)

#Prepare cursor object
cursorObject = dataBase.cursor()

#Create a database
# This is a test comment
cursorObject.execute("CREATE DATABASE Michy")

print("All Done!")
