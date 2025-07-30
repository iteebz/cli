import json
from datetime import datetime
from pathlib import Path
from .storage import get_tasks_dir, save_task

def show_task(task_id):
    tasks_dir = get_tasks_dir()
    task_file = tasks_dir / f"{task_id}.json"
    
    if not task_file.exists():
        print(f"task not found: {task_id}")
        return
    
    try:
        task = json.loads(task_file.read_text())
        print(f"Task: {task['id']}")
        print(f"Created: {task.get('created', 'unknown')}")
        print(f"Status: {task.get('status', 'unknown')}")
        print(f"Priority: {task.get('priority', 'unknown')}")
        print()
        print(task.get('ai_enhancement', 'No enhancement available'))
    except Exception as e:
        print(f"error reading task: {e}")

def update_task(task_id, status):
    tasks_dir = get_tasks_dir()
    task_file = tasks_dir / f"{task_id}.json"
    
    if not task_file.exists():
        print(f"task not found: {task_id}")
        return
    
    try:
        task = json.loads(task_file.read_text())
        old_status = task.get("status", "unknown")
        task["status"] = status
        task["updated"] = datetime.now().isoformat()
        
        if status == "done":
            task["completed"] = datetime.now().isoformat()
        
        save_task(task)
        print(f"task {task_id}: {old_status} → {status}")
        
    except Exception as e:
        print(f"error updating task: {e}")