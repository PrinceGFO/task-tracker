# Task Tracker API - Core Logic - PrinceGFO

tasks = []

def create_task(title, status="pending"):
    task = {"id": len(tasks)+1, "title": title, "status": status}
    tasks.append(task)
    return task

def get_tasks(status=None):
    if status:
        return [t for t in tasks if t["status"] == status]
    return tasks

def update_task(task_id, status):
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = status
            return t
    return None

# Demo
create_task("Setup FastAPI project")
create_task("Add JWT Auth", "in_progress")
create_task("Write tests", "pending")

print("All tasks:", get_tasks())
print("Pending:", get_tasks("pending"))

update_task(1, "completed")
print("After update:", get_tasks())
