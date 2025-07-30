# Refactor - AI-Powered Code Refactoring

A clean, simple code refactoring CLI powered by Cogency. Analyze, clean up, and modernize your codebase with zero ceremony.

## Features

- **Code analysis** - AI identifies refactoring opportunities and code smells
- **File cleanup** - AI refactors individual files with safety backups
- **Function extraction** - AI suggests breaking down complex functions
- **Code modernization** - AI recommends modern language features
- **Architecture review** - AI analyzes project structure and organization

## Usage

```bash
# Analyze current directory for refactoring opportunities
python main.py
python main.py analyze

# Analyze specific file or directory
python main.py analyze src/
python main.py analyze myfile.py

# Clean up and refactor a specific file (with backup)
python main.py cleanup myfile.py

# Analyze file for function extraction opportunities
python main.py extract myfile.py

# Get modernization suggestions
python main.py modernize
python main.py modernize src/

# Review architecture and project structure
python main.py arch
python main.py arch src/
```

## Magic Interface

The refactor tool supports a "magic" interface - any path argument that doesn't match commands is analyzed:

```bash
python main.py src/components/
# Analyzes the components directory for refactoring opportunities
```

## Supported Languages

- Python (.py)
- JavaScript (.js)
- TypeScript (.ts, .tsx)
- React (.jsx)
- Java (.java)
- Go (.go)
- Rust (.rs)

## Safety Features

- **Backup creation** - Original files are backed up before changes
- **Preview mode** - Shows proposed changes before applying
- **User confirmation** - Requires explicit approval for file modifications
- **Error handling** - Graceful failures with helpful messages

## Cogency Integration

This tool demonstrates clean Cogency usage with a single agent type:

```python
# Single agent for all refactoring tasks
agent = Agent("code-refactor")

# Code analysis
result = agent.run(f"analyze this codebase for refactoring opportunities: {code}")

# File cleanup
result = agent.run(f"refactor and clean up this code: {content}")

# Function extraction
result = agent.run(f"analyze for function extraction opportunities: {content}")

# Modernization
result = agent.run(f"suggest modernization improvements: {content}")

# Architecture review
result = agent.run(f"analyze project structure and suggest improvements: {structure}")
```

## Key Design Principles

- **150 lines total** - Comprehensive refactoring in minimal code
- **Single file** - Easy to understand and modify
- **Direct Cogency usage** - Shows the core Agent pattern
- **Safety first** - Backups and confirmations prevent data loss
- **Multi-language support** - Works across different programming languages
- **Practical utility** - Actually useful for daily development work

Perfect for code reviews, technical debt reduction, legacy code modernization, and maintaining code quality standards.