#!/usr/bin/env python3
"""goals - dreams with ai"""

from src.shared.storage import Storage, create_item
from src.shared.cli import run_cli, print_items
from src.shared.insights import Insights

storage = Storage("goals")

def create_goal(args):
    if not args:
        print("usage: goals create \"description\"")
        return
    
    description = " ".join(args)
    print(f"creating: {description}")
    
    try:
        ai_analysis = Insights.goal_insights(description)
        goal = create_item("goals", description, status="active", ai_analysis=ai_analysis)
        storage.save(goal)
        print(f"created: {goal['id']}")
    except Exception as e:
        print(f"error: {e}")

def list_goals(args=None):
    goals = storage.load_all()
    print_items(goals, "goals")

def show_goal(args):
    if not args:
        print("usage: goals show <id>")
        return
    
    goal = storage.load_one(args[0])
    if not goal:
        print(f"not found: {args[0]}")
        return
    
    print(f"goal: {goal['id']}")
    print(f"status: {goal.get('status')}")
    print()
    print(goal.get('ai_analysis', 'no analysis'))

def complete_goal(args):
    if not args:
        print("usage: goals complete <id>")
        return
    
    if storage.update(args[0], {"status": "completed"}):
        print(f"completed: {args[0]}")
    else:
        print(f"not found: {args[0]}")

def magic_create(args):
    return create_goal(args)

commands = {
    "create": create_goal,
    "list": list_goals,
    "show": show_goal,
    "complete": complete_goal
}

def main():
    run_cli("goals", commands, magic_create)

if __name__ == "__main__":
    main()