from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title. Must be a non-empty string.")
        return
    if not validate_task_description(description):
        print("Invalid description. Must be a non-empty string.")
        return
    if not validate_due_date(due_date):
        print("Invalid due date. Use YYYY-MM-DD format.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return
    for i, task in enumerate(pending, start=1):
        print(f"{i}. {task['title']} - {task['description']} (Due: {task['due_date']})")

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    completed_count = sum(1 for t in tasks if t["completed"])
    progress = (completed_count / len(tasks)) * 100
    return progress
