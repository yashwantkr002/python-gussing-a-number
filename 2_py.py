class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            status = " [X] " if task["completed"] else " [ ] "
            print(f"{i + 1}. {status}{task['task']}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nSelect an option:")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. Remove a task")
        print("4. View to-do list")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "3":
            index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
