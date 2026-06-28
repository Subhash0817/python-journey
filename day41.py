import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
conn.commit()


class EmployeeManagement:

    def add_employee(self, name, department, salary):
        cursor.execute(
            "INSERT INTO employees(name, department, salary) VALUES (?, ?, ?)",
            (name, department, salary)
        )
        conn.commit()
        print("✅ Employee added successfully!")

    def view_employees(self):
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        if employees:
            print("\n----- Employees -----")
            for emp in employees:
                print(f"ID: {emp[0]}")
                print(f"Name: {emp[1]}")
                print(f"Department: {emp[2]}")
                print(f"Salary: ₹{emp[3]}")
                print("-" * 25)
        else:
            print("No employees found.")

    def update_salary(self, emp_id, salary):
        cursor.execute(
            "UPDATE employees SET salary=? WHERE id=?",
            (salary, emp_id)
        )
        conn.commit()
        print("✅ Salary updated successfully!")

    def delete_employee(self, emp_id):
        cursor.execute(
            "DELETE FROM employees WHERE id=?",
            (emp_id,)
        )
        conn.commit()
        print("✅ Employee deleted successfully!")


system = EmployeeManagement()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))
        system.add_employee(name, department, salary)

    elif choice == "2":
        system.view_employees()

    elif choice == "3":
        emp_id = int(input("Enter employee ID: "))
        salary = float(input("Enter new salary: "))
        system.update_salary(emp_id, salary)

    elif choice == "4":
        emp_id = int(input("Enter employee ID: "))
        system.delete_employee(emp_id)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")

conn.close()