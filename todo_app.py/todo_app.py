import json
import os

TASKS_FILE = "tasks.json"

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self):
        task = input("Enter task description: ")
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
        print("Task added!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. [{status}] {task['task']}")

    def mark_done(self):
        self.list_tasks()
        try:
            idx = int(input("Enter task number to mark as done: "))
            if 1 <= idx <= len(self.tasks):
                self.tasks[idx-1]["done"] = True
                self.save_tasks()
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        self.list_tasks()
        try:
            idx = int(input("Enter task number to delete: "))
            if 1 <= idx <= len(self.tasks):
                del self.tasks[idx-1]
                self.save_tasks()
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            print("\nTodo List Menu:")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Mark Task as Done")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.mark_done()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Bye!")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
