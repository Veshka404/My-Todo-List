class TodoApp:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_tasks(self, description):
        task_id = self.next_id
        self.tasks[task_id] = {'description': description, 'completed': False}
        self.next_id += 1
        print(f"Task '{description}' added with ID {task_id}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task_id, task in self.tasks.items():
            status = "✔" if task['completed'] else "✘"
            print(f"{task_id}: {task['description']} - {status}")

    def mark_complete(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Task '{removed_task['description']}' deleted.")
        else:
            print(f"Task ID {task_id} not found.")

# Main program loop
if __name__ == "__main__":
    app = TodoApp()

    while True:
        print("\nOptions: add, view, complete, delete, quit")
        action = input("Choose an option: ").strip().lower()

        if action == "add":
            description = input("Enter task description: ")
            app.add_tasks(description)
        elif action == "view":
            app.view_tasks()
        elif action == "complete":
            task_id = int(input("Enter task ID to mark complete: "))
            app.mark_complete(task_id)
        elif action == "delete":
            task_id = int(input("Enter task ID to delete: "))
            app.delete_task(task_id)
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
