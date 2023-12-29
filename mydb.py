import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Manav"
    
)

# prepare a cursor object using cursor() method

cursorObject = dataBase.cursor()

#  create a database

cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")