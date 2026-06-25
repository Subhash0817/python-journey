import sqlite3


class ExpenseTracker:

    def __init__(self):

        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT
        )
        """)

        self.conn.commit()

    def add_expense(self):

        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")

        self.cursor.execute(
            "INSERT INTO expenses(amount, category) VALUES(?, ?)",
            (amount, category)
        )

        self.conn.commit()

        print("Expense Added Successfully")

    def view_expenses(self):

        self.cursor.execute(
            "SELECT * FROM expenses"
        )

        expenses = self.cursor.fetchall()

        if not expenses:

            print("No Expenses Found")
            return

        for expense in expenses:

            print(
                f"ID: {expense[0]} | "
                f"Amount: ₹{expense[1]} | "
                f"Category: {expense[2]}"
            )

    def total_expense(self):

        self.cursor.execute(
            "SELECT SUM(amount) FROM expenses"
        )

        total = self.cursor.fetchone()[0]

        print(f"Total Expense: ₹{total or 0}")

    def delete_expense(self):

        expense_id = int(input("Enter Expense ID: "))

        self.cursor.execute(
            "DELETE FROM expenses WHERE id=?",
            (expense_id,)
        )

        self.conn.commit()

        print("Expense Deleted Successfully")


tracker = ExpenseTracker()

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        tracker.delete_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")