from datetime import datetime
from cogency import Agent
from .storage import save_task

def create_task(description, priority="medium"):
    if not description.strip():
        print("error: task description required")
        return
    
    print(f"creating task: {description}")
    
    try:
        agent = Agent("task-enhancer")
        result = agent.run(f"""Enhance this task description: {description}

Return a structured task with:
- title: clear, actionable task title
- description: expanded description with context
- estimated_time: realistic time estimate (minutes/hours)
- difficulty: easy/medium/hard
- category: type of work (coding, writing, research, admin, etc.)
- prerequisites: what needs to be done first
- success_criteria: how to know it's complete
- next_steps: immediate actions to start

Make it specific and actionable.""")
        
        task_id = datetime.now().strftime("%Y%m%d-%H%M%S")
        task = {
            "id": task_id,
            "created": datetime.now().isoformat(),
            "status": "todo",
            "priority": priority,
            "description": description,
            "ai_enhancement": result.response
        }
        
        save_task(task)
        print(f"created task: {task_id}")
        
    except Exception as e:
        print(f"error creating task: {e}")