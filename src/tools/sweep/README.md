# Sweep - AI-Powered Obsidian Vault Cleanup

Clean, focused Obsidian vault management powered by Cogency. Demonstrates AI-driven content analysis in under 150 lines.

## Features

- **Smart analysis** - AI identifies vault issues and cleanup opportunities
- **Intelligent cleanup** - AI-powered note formatting with automatic backups
- **Duplicate detection** - Find exact duplicate content across your vault
- **Consistent formatting** - AI-driven markdown style consistency
- **Organization insights** - AI recommendations for better vault structure

## Usage

```bash
# Analyze vault (default action)
python main.py
python main.py analyze ~/my-vault

# Clean up notes with AI
python main.py clean ~/my-vault

# Find duplicates
python main.py duplicates ~/my-vault

# Format notes consistently
python main.py format ~/my-vault

# Get organization recommendations  
python main.py organize ~/my-vault
```

## Magic Interface

Any path argument analyzes that vault:

```bash
python main.py ~/Documents/MyVault
# Analyzes the specified vault
```

## Core Cogency Patterns

```python
# Vault analysis
agent = Agent("vault-analyzer")
result = agent.run(f"Analyze these Obsidian notes: {content}")

# Note cleaning
agent = Agent("note-cleaner")
result = agent.run(f"Clean up this Obsidian note: {content}")

# Organization planning
agent = Agent("vault-organizer")
result = agent.run(f"Suggest folder organization: {content}")
```

## Design Principles

- **Under 150 lines** - Focused, clean implementation
- **Single file** - Easy to understand and modify
- **Direct Cogency usage** - Clear Agent patterns
- **Safe operations** - Always backup before changes
- **Practical utility** - Actually useful for vault maintenance

Perfect example of AI-powered content analysis with Cogency's simple, powerful interface.