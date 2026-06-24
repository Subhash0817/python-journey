import sqlite3


class TaskManager:

    def __init__(self):

        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            completed INTEGER
        )
        """)

        self.conn.commit()

    def add_task(self):

        task = input("Enter Task: ")

        self.cursor.execute(
            "INSERT INTO tasks(task, completed) VALUES(?, ?)",
            (task, 0)
        )

        self.conn.commit()

        print("Task Added Successfully")

    def view_tasks(self):

        self.cursor.execute(
            "SELECT * FROM tasks"
        )

        tasks = self.cursor.fetchall()

        if not tasks:

            print("No Tasks Found")

            return

        for task in tasks:

            status = "✓" if task[2] else "✗"

            print(
                f"ID: {task[0]} | "
                f"Task: {task[1]} | "
                f"Status: {status}"
            )

    def complete_task(self):

        task_id = int(input("Enter Task ID: "))

        self.cursor.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )

        self.conn.commit()

        print("Task Completed")

    def delete_task(self):

        task_id = int(input("Enter Task ID: "))

        self.cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        self.conn.commit()

        print("Task Deleted")


manager = TaskManager()

while True:

    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_task()

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        manager.complete_task()

    elif choice == "4":
        manager.delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")