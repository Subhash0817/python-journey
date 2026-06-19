import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")

def add_student():
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )

    conn.commit()
    print("Student Added Successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\nStudent Records")
    print("-" * 30)

    for student in students:
        print(student)

def update_marks():
    student_id = int(input("Enter Student ID: "))
    new_marks = int(input("Enter New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (new_marks, student_id)
    )

    conn.commit()
    print("Marks Updated Successfully!")

def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    print("Student Deleted Successfully!")

while True:
    print("\n===== Student Database System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_marks()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")

conn.close()