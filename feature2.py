def list_tasks():
    print("\nTo-Do List (incomplete):")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['description']} [{status}]")
    print()
