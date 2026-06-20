import sqlite3

class StudentDB:

    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_no INTEGER,
            marks INTEGER
        )
        """)

        self.conn.commit()

    def add_student(self):

        name = input("Enter Name: ")
        roll_no = int(input("Enter Roll No: "))
        marks = int(input("Enter Marks: "))

        self.cursor.execute(
            "INSERT INTO students(name, roll_no, marks) VALUES(?,?,?)",
            (name, roll_no, marks)
        )

        self.conn.commit()

        print("Student Added Successfully")

    def view_students(self):

        self.cursor.execute("SELECT * FROM students")

        students = self.cursor.fetchall()

        for student in students:
            print(student)

    def search_student(self):

        name = input("Enter Name: ")

        self.cursor.execute(
            "SELECT * FROM students WHERE name=?",
            (name,)
        )

        student = self.cursor.fetchall()

        if student:
            for s in student:
                print(s)
        else:
            print("Student Not Found")

    def update_marks(self):

        roll_no = int(input("Enter Roll No: "))
        marks = int(input("Enter New Marks: "))

        self.cursor.execute(
            "UPDATE students SET marks=? WHERE roll_no=?",
            (marks, roll_no)
        )

        self.conn.commit()

        print("Marks Updated Successfully")

    def delete_student(self):

        roll_no = int(input("Enter Roll No: "))

        self.cursor.execute(
            "DELETE FROM students WHERE roll_no=?",
            (roll_no,)
        )

        self.conn.commit()

        print("Student Deleted Successfully")
    def show_topper(self):

        self.cursor.execute(
        "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
    )

        topper = self.cursor.fetchone()

        if topper:
            print("\nTopper Details:")
            print(topper)
        else:
            print("No students found")
db = StudentDB()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        db.add_student()

    elif choice == "2":
        db.view_students()

    elif choice == "3":
        db.search_student()

    elif choice == "4":
        db.update_marks()

    elif choice == "5":
        db.delete_student()

    elif choice == "6":
        db.show_topper()

    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")