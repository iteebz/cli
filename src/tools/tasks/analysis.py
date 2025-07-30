from cogency import Agent
from .storage import load_tasks

def prioritize_tasks():
    tasks = load_tasks()
    active_tasks = [t for t in tasks if t.get("status") in ["todo", "in_progress"]]
    
    if not active_tasks:
        print("no active tasks to prioritize")
        return
    
    print("prioritizing tasks with AI...")
    
    try:
        tasks_summary = "\n".join([
            f"Task {t['id']}: {t.get('description', '')} (current priority: {t.get('priority', 'medium')})"
            for t in active_tasks
        ])
        
        agent = Agent("task-prioritizer")
        result = agent.run(f"""Analyze and prioritize these tasks:

{tasks_summary}

Consider:
- Impact on goals and objectives
- Urgency and deadlines
- Dependencies between tasks
- Effort required vs. value delivered

Provide:
1. Recommended priority order (high/medium/low)
2. Reasoning for each priority assignment
3. Suggested task sequencing
4. Quick wins to tackle first""")
        
        print(result.response)
        
    except Exception as e:
        print(f"error prioritizing tasks: {e}")

def focus_session():
    tasks = load_tasks()
    high_priority = [t for t in tasks if t.get("priority") == "high" and t.get("status") == "todo"]
    
    if not high_priority:
        print("no high-priority tasks available")
        return
    
    print("starting focus session...")
    print(f"high-priority tasks ({len(high_priority)}):")
    
    for i, task in enumerate(high_priority[:3], 1):  # Top 3
        print(f"{i}. {task['id']} - {task.get('description', '')}")
    
    print("\nrecommended focus order based on AI analysis")