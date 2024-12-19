from pymongo import MongoClient
import json

def read_data():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    return config

config = read_data()
client = MongoClient(config["connection"])
db = client[config["db_name"]]
students = db[config["students_collection"]]
print("Connected")

def add_student_records():
    st_id = input("Enter the student ID: ")
    student = students.find_one({"student_id": st_id})
    if student:
        print(f"Student with ID {st_id} already exists.")
        return

    st_name = input("Enter the student name: ")
    st_age = input("Enter the student age: ")
    
    if not st_age.isdigit():
        print("Invalid age. Please enter a numeric value.")
        return

    student = {
        "student_id": st_id,
        "student_name": st_name,
        "student_age": int(st_age)
    }

    students.insert_one(student)
    print("Student record added successfully!")

def remove_student_records():
    st_id = input("Enter the student ID to remove: ")
    result = students.delete_one({"student_id": st_id})
    if result.deleted_count > 0:
        print(f"Student with ID {st_id} has been removed.")
    else:
        print(f"No student found with ID {st_id}.")

def search_for_students_records():
    st_id = input("Enter the student ID to search for: ")
    student = students.find_one({"student_id": st_id})
    if student:
        print("Student found:")
        print(f"ID: {student['student_id']}, Name: {student['student_name']}, Age: {student['student_age']}")
    else:
        print(f"No student found with ID {st_id}.")

def display_students_details():
    all_students = students.find()
    print("\nStudents details:")
    for student in all_students:
        print(f"ID: {student['student_id']}, Name: {student['student_name']}, Age: {student['student_age']}")

def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. Add student records")
        print("2. Remove student records")
        print("3. Search for student records")
        print("4. Display student details")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student_records()
        elif choice == "2":
            remove_student_records()
        elif choice == "3":
            search_for_students_records()
        elif choice == "4":
            display_students_details()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
