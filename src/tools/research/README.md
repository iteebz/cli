# Research - AI-Powered Research Assistant

A clean, simple research CLI powered by Cogency. Collect sources, synthesize insights, and export findings with zero ceremony.

## Features

- **Smart source analysis** - AI extracts insights from URLs and files
- **Research synthesis** - AI combines findings across sources
- **Question answering** - Ask specific questions about your research
- **Export reports** - Generate markdown research reports
- **Session management** - Persistent research sessions

## Usage

```bash
# Start a new research session
python main.py "impact of AI on software development"

# Add sources (URLs or files)
python main.py add https://example.com/article
python main.py add research-paper.pdf
python main.py add notes.txt

# List current sources
python main.py list

# Synthesize all research
python main.py synthesize

# Ask specific questions
python main.py ask "what are the main benefits?"
python main.py ask "what challenges were identified?"

# Export research report
python main.py export
python main.py export my-research-report.md

# Check session status
python main.py

# Clear current session
python main.py clear
```

## Magic Interface

The research tool supports a "magic" interface - any arguments that don't match commands start a new research session:

```bash
python main.py "machine learning trends 2024"
# Starts a new research session on that topic
```

## File Structure

Research data is stored in a `research/` directory:
- `session.json` - Current research session data
- `research-topic-20240130.md` - Exported reports

## Cogency Integration

This tool demonstrates clean Cogency usage with a single agent type:

```python
# Simple agent for all research tasks
agent = Agent("research-assistant")

# URL analysis
result = agent.run(f"research this URL for insights on '{topic}': {url}")

# Document analysis  
result = agent.run(f"analyze this document for insights on '{topic}':\n\n{content}")

# Synthesis
result = agent.run(f"synthesize research on '{topic}' from these sources:\n\n{sources}")

# Q&A
result = agent.run(f"answer this question about '{topic}': {question}\n\nBased on: {sources}")
```

## Key Design Principles

- **150 lines total** - Maximum utility with minimal complexity
- **Single file** - Easy to understand and modify
- **Direct Cogency usage** - Shows the core Agent pattern
- **Persistent sessions** - Research builds over time
- **Clean error handling** - Graceful failures with helpful messages
- **Export capability** - Generate shareable research reports

Perfect for academic research, market analysis, competitive intelligence, or any topic requiring systematic source collection and analysis.