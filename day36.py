class Task:

    def __init__(self, title):
        self.title = title
        self.completed = False


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):

        with open("tasks.txt", "w") as file:

            for task in self.tasks:

                file.write(
                    f"{task.title},{task.completed}\n"
                )

    def load_tasks(self):

        try:

            with open("tasks.txt", "r") as file:

                for line in file:

                    title, completed = line.strip().split(",")

                    task = Task(title)

                    task.completed = completed == "True"

                    self.tasks.append(task)

        except FileNotFoundError:

            pass

    def add_task(self):

        title = input("Enter Task: ")

        self.tasks.append(Task(title))

        self.save_tasks()

        print("Task Added Successfully")

    def view_tasks(self):

        if not self.tasks:

            print("No Tasks Found")

            return

        for i, task in enumerate(self.tasks, start=1):

            status = "✓" if task.completed else "✗"

            print(f"{i}. {task.title} [{status}]")

    def complete_task(self):

        self.view_tasks()

        task_no = int(input("Enter Task Number: "))

        if 1 <= task_no <= len(self.tasks):

            self.tasks[task_no - 1].completed = True

            self.save_tasks()

            print("Task Completed")

    def delete_task(self):

        self.view_tasks()

        task_no = int(input("Enter Task Number: "))

        if 1 <= task_no <= len(self.tasks):

            self.tasks.pop(task_no - 1)

            self.save_tasks()

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