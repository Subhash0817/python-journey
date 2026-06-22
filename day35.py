class Expense:

    def __init__(self, amount, category):
        self.amount = amount
        self.category = category


class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def add_expense(self):

        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")

        expense = Expense(amount, category)

        self.expenses.append(expense)

        print("Expense Added Successfully")

    def view_expenses(self):

        if not self.expenses:
            print("No Expenses Found")
            return

        for expense in self.expenses:

            print(
                f"Amount: ₹{expense.amount} | "
                f"Category: {expense.category}"
            )

    def total_expense(self):

        total = 0

        for expense in self.expenses:

            total += expense.amount

        print(f"Total Expense: ₹{total}")

    def category_wise_expense(self):

        category = input("Enter Category: ")

        total = 0

        for expense in self.expenses:

            if expense.category.lower() == category.lower():

                total += expense.amount

        print(f"{category} Expense: ₹{total}")


tracker = ExpenseTracker()

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Wise Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        tracker.category_wise_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")