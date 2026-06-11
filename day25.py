class Student:

    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    def show_name(self):
        print("Name:", self.name)

    @classmethod
    def show_total_students(cls):
        print("Total Students:", cls.total_students)


student1 = Student("Subhash")
student2 = Student("Rahul")
student3 = Student("Sai")

student1.show_name()
student2.show_name()
student3.show_name()

Student.show_total_students()