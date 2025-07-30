# goals - AI-Powered Goal Setting

Transform vague aspirations into structured, actionable goals with AI assistance.

## Quick Start

```bash
# Create a goal (AI enhances it)
python main.py create "learn machine learning"

# Or just start typing
python main.py "get better at public speaking"

# List all goals
python main.py

# Review progress with AI
python main.py review
```

## Commands

### Goal Creation
```bash
goals create "goal description"    # AI structures your goal
goals "learn python"              # Magic interface - just describe it
```

### Goal Management
```bash
goals list                        # Show all goals
goals show 20240730-1234          # Detailed goal view
goals complete 20240730-1234      # Mark as completed
goals pause 20240730-1234         # Pause goal
```

### AI Analysis
```bash
goals review                      # AI reviews all goals and suggests improvements
```

## What It Does

**AI Enhancement**: Takes your rough goal description and creates a structured SMART goal with:
- Clear, actionable title
- Expanded description with context
- Category classification (career, health, learning, etc.)
- Realistic timeframe
- Specific success criteria
- Immediate next actions

**Progress Tracking**: Simple status management (active, completed, paused)

**AI Review**: Periodic analysis of your goal portfolio with recommendations

## File Structure

Goals are stored as JSON files in `goals/`:
```
goals/
├── 20240730-1234.json    # Individual goal files
├── 20240730-1456.json
└── ...
```

Each goal contains:
- Unique ID and timestamps
- Status tracking
- AI-generated structure and analysis

## Examples

### Input
```bash
goals "lose weight"
```

### AI Output
```json
{
  "title": "Lose 15 pounds through sustainable lifestyle changes",
  "description": "Achieve healthy weight loss through balanced nutrition and regular exercise",
  "category": "health",
  "timeframe": "3 months",
  "success_criteria": [
    "Lose 1-2 pounds per week consistently",
    "Establish 4x/week exercise routine",
    "Track daily nutrition intake"
  ],
  "next_actions": [
    "Calculate target calorie deficit",
    "Plan weekly meal prep schedule",
    "Choose 3 enjoyable forms of exercise"
  ]
}
```

## Integration

Goals integrate with other tools through shared filesystem:
- **plans** can reference goal IDs
- **tasks** can be linked to specific goals
- **manage** can coordinate goal-related workflows

## Philosophy

- **AI-Enhanced**: Turn vague ideas into structured goals
- **Filesystem-Based**: Simple JSON storage for easy integration
- **SMART Goals**: AI ensures goals are Specific, Measurable, Achievable, Relevant, Time-bound
- **Review-Driven**: Regular AI analysis keeps you on track

Transform "I want to..." into "I will achieve X by Y through Z."