#Author: Fedele Colosimo
#Module 13 Final
#This program allows the user to add, edit, and delete tasks, set priorities, and mark task complete.

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} [Priority: {self.priority}] - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
        print("Task added successfully.")

    def edit_task(self, task_id, new_description=None, new_priority=None):
        if 0 <= task_id < len(self.tasks):
            if new_description:
                self.tasks[task_id].description = new_description
            if new_priority:
                self.tasks[task_id].priority = new_priority
            print("Task edited successfully.")
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks.pop(task_id)
            print("Task deleted successfully.")
        else:
            print("Invalid task ID.")

    def mark_task_complete(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].completed = True
            print("Task marked as complete.")
        else:
            print("Invalid task ID.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx}. {task}")


def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Display Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            manager.add_task(description, priority)
        elif choice == '2':
            task_id = int(input("Enter task ID to edit: "))
            new_description = input("Enter new task description (or leave blank to keep current): ")
            new_priority = input("Enter new task priority (or leave blank to keep current): ")
            manager.edit_task(task_id, new_description, new_priority)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.mark_task_complete(task_id)
        elif choice == '5':
            manager.display_tasks()
        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
