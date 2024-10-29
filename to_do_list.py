
tasks = []


def add_task(task):

    tasks = tasks + [task] 
    print(f"Added task: {task}")


def delete_task(task_number):
    task = tasks.pop(task_number)  
    print(f"Deleted task: {task}")
