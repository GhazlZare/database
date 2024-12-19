import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_Password",
    database="university"
)
mycursor = mydb.cursor()

# create the database
# sql = "CREATE DATABASE university"
# mycursor.execute(sql)

# Create tables
'''
sql = """
    CREATE TABLE students(
        st_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        st_name VARCHAR(255) NOT NULL,
        st_Lname VARCHAR(255) NOT NULL,
        birthday DATE NOT NULL,
        email VARCHAR(255) NOT NULL
    );
"""
mycursor.execute(sql)

sql = """
    CREATE TABLE courses(
        c_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        c_name VARCHAR(255) NOT NULL,
        instructor VARCHAR(255) NOT NULL
    );
"""
mycursor.execute(sql)

sql = """
    CREATE TABLE enrollments(
        e_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        st_id INT NOT NULL,
        c_id INT NOT NULL,
        FOREIGN KEY (st_id) REFERENCES students(st_id),
        FOREIGN KEY (c_id) REFERENCES courses(c_id)
    );
"""
try:
    mycursor.execute(sql)
except:
    print("Error")
'''

# Insert values with
'''
sql = """
    INSERT INTO students (st_name, st_Lname, birthday, email) VALUES
    ('Ghazal', 'Zare', '2004-02-14', 'ab@gmail.com'),
    ('Sajede', 'Mohajer', '2004-03-17', 'sj@gmail.com');
"""
try:
    mycursor.execute(sql)
except:
    print("Error")
mydb.commit()

sql = """
    INSERT INTO courses (c_name, instructor) VALUES
    ('Python', 'Ms.Bakhshandeh');
"""
try:
    mycursor.execute(sql)
except:
    print("Error")
mydb.commit()

sql = """
    INSERT INTO enrollments (st_id, c_id) VALUES
    (1, 1);
"""
try:
    mycursor.execute(sql)
except:
    print("Error")
mydb.commit()
'''

# Querying data
sql = """
    SELECT st_name, COUNT(enrollments.c_id) AS course_count
    FROM students 
    LEFT JOIN enrollments ON students.st_id = enrollments.st_id
    GROUP BY students.st_id;
"""
try:
    mycursor.execute(sql)
except:
    print("Error")
print("Student Enrollments:")
for row in mycursor.fetchall():
    print(row)

# Remove
sql = """
    DELETE FROM students 
    WHERE st_id IN (
        SELECT st_id
        FROM (
            SELECT students.st_id, COUNT(enrollments.c_id) AS course_count
            FROM students 
            LEFT JOIN enrollments ON students.st_id = enrollments.st_id
            GROUP BY students.st_id
            HAVING course_count < 2
        ) AS subquery
    );
"""
try:
    mycursor.execute(sql)
except:
    print("Error")
mydb.commit()

# Update courses
sql = """
    UPDATE courses 
    SET c_name = REPLACE(c_name, 'Java', 'Python')
    WHERE c_name LIKE '%Java%';
"""
mycursor.execute(sql)
mydb.commit()

# Close connection
mycursor.close()
mydb.close()
