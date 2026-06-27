import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")

class Student:

    def add_student(self, name, marks):
        cursor.execute(
            "INSERT INTO students(name, marks) VALUES (?, ?)",
            (name, marks)
        )
        conn.commit()
        print("Student Added Successfully!")

    def view_students(self):
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if students:
            for student in students:
                print(student)
        else:
            print("No Students Found")

    def update_marks(self, student_id, marks):
        cursor.execute(
            "UPDATE students SET marks=? WHERE id=?",
            (marks, student_id)
        )
        conn.commit()
        print("Marks Updated Successfully!")

student = Student()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        student.add_student(name, marks)

    elif choice == "2":
        student.view_students()

    elif choice == "3":
        student_id = int(input("Enter Student ID: "))
        marks = int(input("Enter New Marks: "))
        student.update_marks(student_id, marks)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")

conn.close()