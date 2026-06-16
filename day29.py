class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def show_details(self):
            print("Name:", self.name)
            print("Roll No:", self.roll_no)
            print("Marks:", self.marks)

students = []



def save_students():

    file = open("students.txt", "w")

    for student in students:

        file.write(
            f"{student.name},{student.roll_no},{student.marks}\n"
        )

    file.close()

def load_students():

    try:

        file = open("students.txt", "r")

        for line in file:

            name, roll_no, marks = line.strip().split(",")

            student = Student(
                name,
                int(roll_no),
                int(marks)
            )

            students.append(student)

        file.close()

    except FileNotFoundError:
        pass
load_students()
save_students()
while True:

    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. remove Student")
    print("5. Exit")

    choice = input("Enter choice: ")
    if choice == "1":

        name = input("Enter Name: ")
        roll_no = int(input("Enter Roll No: "))
        marks = int(input("Enter Marks: "))
        student = Student(name, roll_no, marks)
        students.append(student)
        print("Student Added")

    elif choice == "2":
        for student in students:
            student.show_details()
            print()
    elif choice == "3":

        search_name = input("Enter Name: ")

        found = False

        for student in students:

            if student.name == search_name:

                student.show_details()

                found = True

        if not found:
            print("Student Not Found")
        
    elif choice == "4":

        name = input("Enter Name: ")

        for student in students:

            if student.name == name:

                students.remove(student)

                print("Student Removed")

                break
    elif choice == "5":

        print("Goodbye")
        break
