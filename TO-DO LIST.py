import json
import os
class TodoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = '✓' if task['completed'] else '✗'
            print(f"{idx}. [{status}] {task['task']}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            print("Invalid task number.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task number.")
def main():
    todo = TodoList()
    while True:
        print("\nTo-Do List:")
        todo.view_tasks()
        print("\nOptions: [1] Add [2] Update [3] Delete [4] Complete [5] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)
        elif choice == '4':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo.mark_completed(index)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
