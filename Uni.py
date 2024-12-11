import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your_Password",
    database = "university"
)
mycursor = mydb.cursor()

#Create new database
#sql = "CREATE DATABASE university"
#mycursor.execute(sql)

#Create Tables
sql = """
        CREATE TABLE students(
        st_id int NOT NULL auto_increment Primary Key,
        st_name varchar(255) NOT NULL,
        st_Lname varchar(255) NOT NULL,
        birthday Date NOT NULL,
        email varchar(255)
        )"""
mycursor.execute(sql)

sql = """
        CREATE TABLE courses(
        c_id int NOT NULL auto_increment,
        c_name varchar(255),
        instructor varchar(255),
        Primary Key (c_id)
        )"""
mycursor.execute(sql)

sql = """
        CREATE TABLE enrollments(
        e_id int NOT NULL auto_increment PRIMARY KEY,
        st_id int,
        c_id int,
        FOREIGN KEY (st_id) REFERENCES students(st_id),
        FOREIGN KEY (c_id) REFERENCES courses(c_id)
        )"""
mycursor.execute(sql)