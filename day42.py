import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")
conn.commit()


class Bank:

    def create_account(self, name, balance):
        cursor.execute(
            "INSERT INTO accounts(name, balance) VALUES (?, ?)",
            (name, balance)
        )
        conn.commit()
        print("✅ Account Created Successfully!")

    def view_accounts(self):
        cursor.execute("SELECT * FROM accounts")
        accounts = cursor.fetchall()

        if accounts:
            print("\n------ Accounts ------")
            for account in accounts:
                print(f"Account No : {account[0]}")
                print(f"Name       : {account[1]}")
                print(f"Balance    : ₹{account[2]}")
                print("-" * 25)
        else:
            print("No accounts found.")

    def deposit(self, account_no, amount):
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_no=?",
            (amount, account_no)
        )
        conn.commit()
        print("✅ Amount Deposited Successfully!")

    def withdraw(self, account_no, amount):
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_no=?",
            (account_no,)
        )

        account = cursor.fetchone()

        if account:
            if account[0] >= amount:
                cursor.execute(
                    "UPDATE accounts SET balance = balance - ? WHERE account_no=?",
                    (amount, account_no)
                )
                conn.commit()
                print("✅ Withdrawal Successful!")
            else:
                print("❌ Insufficient Balance!")
        else:
            print("Account not found!")

    def delete_account(self, account_no):
        cursor.execute(
            "DELETE FROM accounts WHERE account_no=?",
            (account_no,)
        )
        conn.commit()
        print("✅ Account Deleted Successfully!")


bank = Bank()

while True:
    print("\n====== Bank Management System ======")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Delete Account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))
        bank.create_account(name, balance)

    elif choice == "2":
        bank.view_accounts()

    elif choice == "3":
        account_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))
        bank.deposit(account_no, amount)

    elif choice == "4":
        account_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))
        bank.withdraw(account_no, amount)

    elif choice == "5":
        account_no = int(input("Enter Account Number: "))
        bank.delete_account(account_no)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

conn.close()