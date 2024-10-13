# todo.py

import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'], data['category'])
        task.completed = data.get('completed', False)
        return task
# todo.py (continued)

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            return [Task.from_dict(data) for data in tasks_data]
    except FileNotFoundError:
        return []
# todo.py (continued)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task.completed else "❌"
        print(f"{idx}. [{status}] {task.title} - {task.description} (Category: {task.category})")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted_task.title}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
# todo.py (continued)

def main():
    tasks = load_tasks()
    while True:
        print("\n=== Personal To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
