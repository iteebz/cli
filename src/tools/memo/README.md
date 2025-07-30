# Memo - AI-Powered Note Taking

A clean, simple note-taking CLI powered by Cogency. Perfect example of zero-ceremony AI integration.

## Features

- **Smart note creation** - AI generates structured markdown from prompts
- **Daily notes** - Templated daily note creation
- **Note processing** - AI-powered note editing and enhancement
- **Search** - Find notes by content with context
- **Simple interface** - Intuitive commands, no configuration needed

## Usage

```bash
# Create a note with AI assistance
cogency memo create "meeting notes for project kickoff"
memo create "meeting notes for project kickoff"

# Create empty note
cogency memo create

# List all notes
cogency memo list
cogency memo  # same as list

# Create daily note
cogency memo daily

# Process/edit a note with AI
cogency memo process note.md "add action items section"
cogency memo process note.md "fix grammar and formatting"

# View note content
cogency memo process note.md

# Search notes
cogency memo search "project kickoff"
```

## Magic Interface

The memo tool supports a "magic" interface - any arguments that don't match commands are treated as note content:

```bash
cogency memo "quick idea about the new feature"
# Creates a note with AI-generated content about the idea
```

## File Structure

Notes are stored in a `notes/` directory with timestamped filenames:
- `20240130-1430-meeting-notes-project.md` (AI-generated)
- `20240130-1435.md` (empty note)
- `20240130-daily-2024-01-30.md` (daily note)

## Cogency Integration

This tool demonstrates clean Cogency usage:

```python
# Simple agent creation and execution
agent = Agent("note-creator")
result = agent.run(f"create a markdown note about: {prompt}")

# Different agents for different tasks
agent = Agent("note-processor")
result = agent.run(f"process this note with instruction '{instruction}':\n\n{content}")
```

## Key Design Principles

- **150 lines total** - Demonstrates power without complexity
- **Single file** - No ceremony, easy to understand
- **Direct Cogency usage** - Shows the core Agent pattern
- **Practical utility** - Actually useful for daily note-taking
- **Clean error handling** - Graceful failures with helpful messages

This is the gold standard for Cogency CLI demos - maximum utility with minimal code.