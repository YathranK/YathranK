# todo_list.py

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task.completed else "Not Done"
                print(f"{i + 1}. {task.name} - {status}")

    def add_task(self, name):
        """Add a new task to the list."""
        self.tasks.append(Task(name))
        print(f"Added task: {name}")

    def update_task(self, index, name):
        """Update the name of a task."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].name = name
            print(f"Updated task {index + 1} to: {name}")
        else:
            print("Invalid task number.")

    def complete_task(self, index):
        """Mark a task as completed."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Marked task {index + 1} as completed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
   
    while True:
        print("\nTo-Do List:")
        todo_list.show_tasks()
        print("\nCommands:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("\nEnter your choice: ")
       
        if choice == '1':
            name = input("Enter task name: ")
            todo_list.add_task(name)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            name = input("Enter new task name: ")
            todo_list.update_task(index, name)
        elif choice == '3':
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
