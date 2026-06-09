class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def show_details(self):
            print("Name:", self.name)
            print("Roll No:", self.roll_no)
            print("Marks:", self.marks)
    def is_pass(self):
            if self.marks >= 35:
                  print("pass")
            else:
                  print("fail")
student1 = Student("Subhash", 101, 95)
student2 = Student("Rahul", 102, 25)
students = [student1, student2]
for student in students:
    student.show_details()
    student.is_pass()
    print()
