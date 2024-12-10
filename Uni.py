import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "pass"
)
mycursor = mydb.cursor()

#Create new database
sql = "CREATE DATABASE university"
mycursor.execute(sql)