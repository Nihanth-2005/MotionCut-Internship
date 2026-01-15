import csv

FILENAME = 'tasks.csv'

def load_tasks():
    tasks = []
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(FILENAME, 'w', newline='') as file:
        header = ['title', 'description', 'status']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(tasks)

def add_task(tasks, title, description=""):
    tasks.append({'title': title, 'description': description, 'status': 'incomplete'})
    save_tasks(tasks)

def edit_task(tasks, index, title=None, description=None):
    if index >= 0 and index < len(tasks):
        if title:
            tasks[index]['title'] = title
        if description:
            tasks[index]['description'] = description
        save_tasks(tasks)

def delete_task(tasks, index):
    if index >= 0 and index < len(tasks):
        del tasks[index]
        save_tasks(tasks)

def mark_task_complete(tasks, index):
    if index >= 0 and index < len(tasks):
        tasks[index]['status'] = 'COMPLETE'
        save_tasks(tasks)
        
def display_tasks(tasks):
    index = 1
    for task in tasks:
        print(f"{index}. {task['title']} - {task['description']} [{task['status']}]")
        index += 1

def main():
    tasks = load_tasks()
    while True:
        print("\n\nTask Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. View Tasks")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Task title: ")
            description = input("Task description: ")
            add_task(tasks, title, description)
        elif choice == '2':
            index = int(input("Task number to edit: ")) - 1
            title = input("New title (leave blank to keep): ")
            description = input("New description (leave blank to keep): ")
            edit_task(tasks, index, title, description)
        elif choice == '3':
            index = int(input("Task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '4':
            index = int(input("Task number to mark complete: ")) - 1
            mark_task_complete(tasks, index)
        elif choice == '5':
            display_tasks(tasks)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
