#!/usr/bin/env python3
"""plans - strategy with ai"""

import asyncio
from cogency import Agent
from src.shared.storage import Storage, create_item
from src.shared.cli import run_cli, print_items
from src.shared.insights import Insights

storage = Storage("plans")
goals_storage = Storage("goals")

def create_plan_with_timeframe(args, timeframe):
    if not args:
        print(f"usage: plans {timeframe} \"description\"")
        return
    
    description = " ".join(args)
    print(f"creating {timeframe}: {description}")
    
    try:
        goals = goals_storage.load_all()
        goals_context = "\n".join([f"- {g['id']}: {g.get('description', '')}" for g in goals[:3]])
        
        ai_plan = Insights.plan_insights(description, timeframe, goals_context)
        plan = create_item("plans", description, 
                          prefix=timeframe, 
                          type=timeframe, 
                          status="active", 
                          ai_plan=ai_plan)
        storage.save(plan)
        print(f"created: {plan['id']}")
    except Exception as e:
        print(f"error: {e}")

def day_plan(args):
    create_plan_with_timeframe(args, "day")

def week_plan(args):
    create_plan_with_timeframe(args, "week")

def list_plans(args=None):
    plans = storage.load_all()
    if not plans:
        print("no plans")
        return
    
    print(f"plans ({len(plans)}):")
    for plan in plans:
        plan_type = plan.get("type", "unknown")
        status = plan.get("status", "unknown")
        created = plan.get("created", "unknown")[:10]
        title = plan.get("id", "untitled")
        print(f"  {title} - {status} {plan_type} ({created})")

def show_plan(args):
    if not args:
        print("usage: plans show <id>")
        return
    
    plan = storage.load_one(args[0])
    if not plan:
        print(f"not found: {args[0]}")
        return
    
    print(f"plan: {plan['id']}")
    print(f"type: {plan.get('type')}")
    print(f"status: {plan.get('status')}")
    print()
    print(plan.get('ai_plan', 'no plan'))

def connect_plan_to_goal(args):
    if len(args) < 2:
        print("usage: plans connect <plan-id> <goal-id>")
        return
    
    plan_id, goal_id = args[0], args[1]
    
    # check if goal exists
    goal = goals_storage.load_one(goal_id)
    if not goal:
        print(f"goal not found: {goal_id}")
        return
    
    if storage.update(plan_id, {"goal_id": goal_id}):
        print(f"connected plan {plan_id} to goal {goal_id}")
    else:
        print(f"plan not found: {plan_id}")

def generate_tasks_from_plan(args):
    if not args:
        print("usage: plans generate-tasks <plan-id>")
        return
    
    plan = storage.load_one(args[0])
    if not plan:
        print(f"plan not found: {args[0]}")
        return
    
    try:
        agent = Agent("task-generator")
        result = asyncio.run(agent.run(f"break this plan into specific tasks:\n{plan.get('ai_plan', plan.get('description'))}"))
        print("suggested tasks:")
        print(result.response)
    except Exception as e:
        print(f"error: {e}")

def magic_create(args):
    return create_plan_with_timeframe(args, "general")

commands = {
    "day": day_plan,
    "week": week_plan,
    "list": list_plans,
    "show": show_plan,
    "connect": connect_plan_to_goal,
    "generate-tasks": generate_tasks_from_plan
}

def main():
    run_cli("plans", commands, magic_create)

if __name__ == "__main__":
    main()