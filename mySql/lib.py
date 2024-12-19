import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_Password",
    database="library_db"
)
mycursor = mydb.cursor()

# Create tables
sql = """
CREATE TABLE IF NOT EXISTS Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Age INT
)
"""
mycursor.execute(sql)

sql = """
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Position VARCHAR(50)
)
"""
mycursor.execute(sql)

sql = """
CREATE TABLE IF NOT EXISTS Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(200),
    Author VARCHAR(100),
    Year INT,
    Genre VARCHAR(50)
)
"""
mycursor.execute(sql)

# Functions for User Management
def register_member():
    name = input("Enter member name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    try:
        sql = "INSERT INTO Members (Name, Email, Age) VALUES (%s, %s, %s)", (name, email, age)    
        mycursor.execute(sql)
        mydb.commit()
        print("Member registered successfully!")
    except mysql.connector.IntegrityError:
        print("Email already exists. Please use a different email.")

def remove_member():
    email = input("Enter email of the member to remove: ")
    mycursor.execute("DELETE FROM Members WHERE Email = %s", (email,))
    mydb.commit()
    if mycursor.rowcount > 0:
        print("Member removed successfully!")
    else:
        print("Member not found!")

def show_member():
    email = input("Enter email of the member: ")
    mycursor.execute("SELECT * FROM Members WHERE Email = %s", (email,))
    member = mycursor.fetchone()
    if member:
        print(f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}, Age: {member[3]}")
    else:
        print("Member not found!")

# Functions for Employee Management
def add_employee():
    name = input("Enter employee name: ")
    position = input("Enter position: ")
    mycursor.execute("INSERT INTO Employees (Name, Position) VALUES (%s, %s)", (name, position))
    mydb.commit()
    print("Employee added successfully!")

def show_employee():
    name = input("Enter employee name: ")
    mycursor.execute("SELECT * FROM Employees WHERE Name = %s", (name,))
    employee = mycursor.fetchone()
    if employee:
        print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}")
    else:
        print("Employee not found!")

# Functions for Book Management
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    mycursor.execute("INSERT INTO Books (Title, Author, Year, Genre) VALUES (%s, %s, %s, %s)", (title, author, year, genre))
    mydb.commit()
    print("Book added successfully!")

def update_book():
    title = input("Enter title of the book to update: ")
    mycursor.execute("SELECT * FROM Books WHERE Title = %s", (title,))
    book = mycursor.fetchone()
    if book:
        author = input("Enter new author name: ")
        year = int(input("Enter new publication year: "))
        genre = input("Enter new genre: ")
        mycursor.execute(
            "UPDATE Books SET Author = %s, Year = %s, Genre = %s WHERE Title = %s",
            (author, year, genre, title)
        )
        mydb.commit()
        print("Book updated successfully!")
    else:
        print("Book not found!")

# Search Functionality
def search_book():
    title = input("Enter book title to search: ")
    mycursor.execute("SELECT * FROM Books WHERE Title LIKE %s", (f"%{title}%",))
    books = mycursor.fetchall()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Genre: {book[4]}")
    else:
        print("No book found with that title!")

# Main Menu
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Register Member")
        print("2. Remove Member")
        print("3. Show Member")
        print("4. Add Employee")
        print("5. Show Employee")
        print("6. Add Book")
        print("7. Update Book")
        print("8. Search Book")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register_member()
        elif choice == 2:
            remove_member()
        elif choice == 3:
            show_member()
        elif choice == 4:
            add_employee()
        elif choice == 5:
            show_employee()
        elif choice == 6:
            add_book()
        elif choice == 7:
            update_book()
        elif choice == 8:
            search_book()
        elif choice == 9:
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()