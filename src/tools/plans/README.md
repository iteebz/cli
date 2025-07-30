# plans - AI-Powered Strategic Planning

Transform ideas into actionable strategic plans with AI assistance. Bridges the gap between goals and daily tasks.

## Quick Start

```bash
# Create a weekly plan
python main.py week "launch new product feature"

# Create a daily plan
python main.py day "prepare for important presentation"

# Or just describe what you want to plan
python main.py "organize team offsite"

# Review all plans
python main.py review
```

## Commands

### Plan Creation
```bash
plans create "description" [timeframe]  # AI creates structured plan
plans day "daily plan"                  # Focused daily planning
plans week "weekly plan"                # Weekly strategic planning  
plans month "monthly plan"              # Monthly strategic planning
plans "organize event"                  # Magic interface - defaults to weekly
```

### Plan Management
```bash
plans list                             # Show all plans
plans show week-20240730-1234          # Detailed plan view
plans complete week-20240730-1234      # Mark as completed
```

### AI Analysis
```bash
plans review                           # AI reviews all plans and suggests improvements
```

## What It Does

**Strategic Planning**: AI creates comprehensive plans with:
- Clear objectives and milestones
- Resource requirements
- Potential obstacles and mitigation
- Success metrics
- Daily/periodic actions

**Goal Integration**: Automatically considers your existing goals when creating plans

**Multi-Timeframe**: Supports day, week, month, and quarter planning

## File Structure

Plans are stored as JSON files in `plans/`:
```
plans/
├── day-20240730-0800.json      # Daily plans
├── week-20240730-1234.json     # Weekly plans  
├── month-20240730-1456.json    # Monthly plans
└── ...
```

Plans automatically reference goals from `goals/` directory for context.

## Examples

### Input
```bash
plans week "improve team productivity"
```

### AI Output
```json
{
  "title": "Weekly Team Productivity Enhancement Plan",
  "timeframe": "week",
  "objectives": [
    "Identify current productivity bottlenecks",
    "Implement 2-3 quick wins",
    "Establish measurement baseline"
  ],
  "milestones": [
    "Day 1-2: Team productivity audit",
    "Day 3-4: Implement process improvements", 
    "Day 5: Measure and document results"
  ],
  "resources_needed": [
    "Team feedback sessions (2 hours)",
    "Process documentation tools",
    "Productivity metrics dashboard"
  ],
  "potential_obstacles": [
    "Resistance to change",
    "Time constraints during busy periods"
  ],
  "success_metrics": [
    "20% reduction in task completion time",
    "Improved team satisfaction scores"
  ],
  "daily_actions": {
    "Monday": "Conduct team productivity survey",
    "Tuesday": "Analyze current workflows",
    "Wednesday": "Implement top 2 improvements",
    "Thursday": "Train team on new processes",
    "Friday": "Measure results and plan next steps"
  }
}
```

## Plan Types

### Daily Plans
- Focused execution plans for single days
- Detailed hour-by-hour scheduling
- Specific deliverables and checkpoints

### Weekly Plans  
- Strategic initiatives spanning a week
- Balanced objectives with daily actions
- Progress milestones and adjustments

### Monthly Plans
- Larger strategic initiatives
- Multiple interconnected objectives
- Resource planning and risk management

## Integration

Plans integrate with the broader ecosystem:
- **goals**: References existing goals for context
- **tasks**: Plans can generate specific tasks
- **manage**: Coordinate plan execution across agents

## Philosophy

- **Strategic Thinking**: AI helps think through complex initiatives
- **Goal-Aligned**: Plans automatically consider your existing goals
- **Actionable**: Every plan includes specific daily actions
- **Realistic**: AI considers timeframes and resource constraints

Turn "I need to..." into "Here's exactly how I'll achieve it."