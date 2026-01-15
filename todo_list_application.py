import csv

FILENAME = "tasks.csv"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "description", "status"])
        writer.writeheader()
        writer.writerows(tasks)

def display_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {task['description']} [{task['status']}]")

tasks = load_tasks()

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Complete\n4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        title = input("Title: ")
        desc = input("Description: ")
        tasks.append({"title": title, "description": desc, "status": "incomplete"})
        save_tasks(tasks)

    elif choice == "2":
        display_tasks(tasks)

    elif choice == "3":
        display_tasks(tasks)
        idx = int(input("Task number: ")) - 1
        tasks[idx]["status"] = "complete"
        save_tasks(tasks)

    elif choice == "4":
        break
