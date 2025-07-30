# tasks - AI-Enhanced Task Management

Transform simple task descriptions into structured, actionable work items with AI assistance.

## Quick Start

```bash
# Create a task (AI enhances it)
python main.py create "fix login bug"

# Or just describe what needs doing
python main.py "write project documentation"

# List tasks by status
python main.py todo                    # Show pending tasks
python main.py done                    # Show completed tasks

# Get AI prioritization help
python main.py prioritize
```

## Commands

### Task Creation
```bash
tasks create "description" [priority]   # AI enhances task details
tasks add "write tests" high           # Create high-priority task
tasks "debug performance issue"        # Magic interface - just describe it
```

### Task Management
```bash
tasks list [status]                    # Show all tasks or filter by status
tasks todo                            # Show pending tasks
tasks done                            # Show completed tasks
tasks show 20240730-123456            # Detailed task view
```

### Task Execution
```bash
tasks start 20240730-123456           # Mark task as in progress
tasks complete 20240730-123456        # Mark task as done
tasks finish 20240730-123456          # Alias for complete
```

### AI Assistance
```bash
tasks prioritize                      # AI analyzes and prioritizes all tasks
tasks focus                          # Start focused session on high-priority tasks
```

## What It Does

**AI Enhancement**: Takes your basic task description and creates structured details:
- Clear, actionable title
- Expanded description with context
- Realistic time estimates
- Difficulty assessment
- Category classification
- Prerequisites and dependencies
- Success criteria
- Immediate next steps

**Smart Prioritization**: AI analyzes tasks considering:
- Impact on goals and objectives
- Urgency and deadlines
- Dependencies between tasks
- Effort vs. value ratio

**Focus Sessions**: Helps you tackle high-priority work with AI-guided task sequencing

## File Structure

Tasks are stored as JSON files in `tasks/`:
```
tasks/
├── 20240730-123456.json    # Individual task files
├── 20240730-123457.json
└── ...
```

Tasks can reference goals and plans from their respective directories for context.

## Examples

### Input
```bash
tasks "optimize database queries"
```

### AI Output
```json
{
  "title": "Optimize slow database queries for user dashboard",
  "description": "Identify and optimize the slowest database queries affecting user dashboard load times",
  "estimated_time": "4-6 hours",
  "difficulty": "medium",
  "category": "performance optimization",
  "prerequisites": [
    "Access to database performance monitoring tools",
    "Understanding of current query patterns"
  ],
  "success_criteria": [
    "Dashboard load time reduced by 50%",
    "Query execution time under 200ms",
    "No regression in data accuracy"
  ],
  "next_steps": [
    "Run database performance analysis",
    "Identify top 5 slowest queries",
    "Create query optimization plan"
  ]
}
```

## Task Lifecycle

```
todo → in_progress → done
  ↑         ↓
  └─── (can revert)
```

**Status Meanings**:
- `todo`: Ready to work on
- `in_progress`: Currently being worked on
- `done`: Completed successfully

## Priority Levels

- 🔥 **high**: Urgent, important, or blocking other work
- 📋 **medium**: Standard priority (default)
- 📝 **low**: Nice to have, can be deferred

## Integration

Tasks integrate with the broader productivity ecosystem:
- **goals**: Tasks can be linked to specific goals
- **plans**: Plans can generate tasks automatically
- **manage**: Coordinate task execution across agents

## Philosophy

- **AI-Enhanced**: Turn vague todos into structured work items
- **Context-Aware**: AI considers your goals and plans
- **Execution-Focused**: Every task includes clear next steps
- **Priority-Driven**: AI helps focus on what matters most

Transform "I need to do..." into "Here's exactly what to do and how."