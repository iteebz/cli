#!/usr/bin/env python3
"""tasks - todos with ai"""

from datetime import datetime
from src.shared.storage import Storage, create_item, find_by_short_id
from src.shared.cli import run_cli, print_items
from src.shared.insights import Insights

storage = Storage("tasks")

def create_task(args):
    if not args:
        print("usage: tasks create \"description\" [priority]")
        return
    
    priority = "medium"
    if len(args) > 1 and args[-1] in ["high", "medium", "low"]:
        priority = args[-1]
        description = " ".join(args[:-1])
    else:
        description = " ".join(args)
    
    print(f"creating: {description}")
    
    try:
        ai_enhancement = Insights.task_insights(description)
        task = create_item("tasks", description, 
                          status="todo", 
                          priority=priority,
                          ai_enhancement=ai_enhancement)
        storage.save(task)
        print(f"created: {task['id']}")
    except Exception as e:
        print(f"error: {e}")

def list_tasks(args=None):
    tasks = storage.load_all()
    print_items(tasks, "tasks")

def todo_tasks(args):
    tasks = [t for t in storage.load_all() if t.get("status") == "todo"] 
    print_items(tasks, "todo")

def show_task(args):
    if not args:
        print("usage: tasks show <id>")
        return
    
    # try exact match first, then short ID
    task = storage.load_one(args[0]) or find_by_short_id(storage, args[0])
    if not task:
        print(f"not found: {args[0]}")
        return
    
    print(f"task: {task['id']} ({task['id'][:8]})")
    print(f"status: {task.get('status')}")
    print(f"priority: {task.get('priority')}")
    print()
    print(task.get('ai_enhancement', 'no ai enhancement'))

def complete_task(args):
    if not args:
        print("usage: tasks complete <id>")
        return
    
    # try exact match first, then short ID
    task = storage.load_one(args[0]) or find_by_short_id(storage, args[0])
    if not task:
        print(f"not found: {args[0]}")
        return
    
    task_id = task["id"]
    if storage.update(task_id, {"status": "done", "completed": datetime.now().isoformat()}):
        print(f"completed: {task_id[:8]}")
    else:
        print(f"error updating: {task_id[:8]}")

def delete_task(args):
    if not args:
        print("usage: tasks delete <id>")
        return
    
    # try exact match first, then short ID
    task = storage.load_one(args[0]) or find_by_short_id(storage, args[0])
    if not task:
        print(f"not found: {args[0]}")
        return
    
    task_id = task["id"]
    if storage.delete(task_id):
        print(f"deleted: {task_id[:8]}")
    else:
        print(f"error deleting: {task_id[:8]}")

def connect_task_to_plan(args):
    if len(args) < 2:
        print("usage: tasks connect <task-id> <plan-id>")
        return
    
    task_id, plan_id = args[0], args[1]
    
    # check if plan exists
    plans_storage = Storage("plans")
    plan = plans_storage.load_one(plan_id)
    if not plan:
        print(f"plan not found: {plan_id}")
        return
    
    if storage.update(task_id, {"plan_id": plan_id}):
        print(f"connected task {task_id} to plan {plan_id}")
    else:
        print(f"task not found: {task_id}")

def magic_create(args):
    """smart routing - show existing tasks or create new ones"""
    if not args:
        print("tasks - todos with ai")
        print("transforms simple todos into structured, actionable tasks")
        print("try: tasks \"fix login bug\" or tasks todo")
        return
    
    # if single arg looks like task ID, try to show it
    if len(args) == 1:
        task = storage.load_one(args[0]) or find_by_short_id(storage, args[0])
        if task:
            show_task([args[0]])
            return
    
    # otherwise create new task
    return create_task(args)

commands = {
    "create": create_task,
    "list": list_tasks,
    "todo": todo_tasks, 
    "show": show_task,
    "complete": complete_task,
    "done": complete_task,
    "delete": delete_task,
    "rm": delete_task,
    "connect": connect_task_to_plan
}

def main():
    run_cli("tasks", commands, magic_create)

if __name__ == "__main__":
    main()