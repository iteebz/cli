#!/usr/bin/env python3
"""memo - notes with ai"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime
from cogency import Agent

def show_help():
    """Show enhanced help for memo"""
    print("🔧 memo - notes with ai")
    print("   Create AI-enhanced notes, daily journals, and search your thoughts")
    print()
    print("📋 Commands:")
    print("  create [prompt]  - Create a new note (with optional AI enhancement)")
    print("  list            - List all notes")
    print("  daily           - Create today's daily note")
    print("  process <note>  - Process/edit a note with AI")
    print("  search <query>  - Search notes by content")
    print()
    print("📝 Examples:")
    print('  memo "brilliant idea about the new feature"')
    print('  memo daily')
    print('  memo search "project ideas"')
    print('  memo process note.md "add action items section"')
    print()
    print("💡 Tips:")
    print("  • Just type your idea: memo \"your thought\"")
    print("  • Daily notes use structured templates")
    print("  • AI can enhance and organize your notes")
    print("  • All notes are stored as markdown in notes/")

def handle_help_or_empty():
    """Handle help requests and empty commands"""
    args = sys.argv[1:]
    if not args or args[0] in ['-h', '--help', 'help']:
        show_help()
        return True
    return False

def create_note(prompt=None):
    notes_dir = Path("notes")
    notes_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    
    if prompt:
        agent = Agent("note-creator")
        result = asyncio.run(agent.run(f"create a markdown note about: {prompt}"))
        
        slug = "-".join(prompt.lower().split()[:4])
        slug = "".join(c for c in slug if c.isalnum() or c in "-")
        filename = f"{timestamp}-{slug}.md"
        content = result.response
    else:
        filename = f"{timestamp}.md"
        content = f"# note\n\n"
    
    note_path = notes_dir / filename
    note_path.write_text(content)
    print(f"created: {filename}")

def list_notes():
    notes_dir = Path("notes")
    if not notes_dir.exists():
        print("no notes found")
        return
    
    notes = sorted([f.name for f in notes_dir.glob("*.md")])
    if not notes:
        print("no notes found")
        return
    
    for note in notes:
        print(f"  {note}")

def create_daily_note():
    notes_dir = Path("notes")
    notes_dir.mkdir(exist_ok=True)
    
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    filename = f"{today.strftime('%Y%m%d')}-daily-{date_str}.md"
    
    content = f"""# Daily Note - {date_str}

## Today's Focus

## Notes

## Tasks
- [ ] 

## Reflections

"""
    
    note_path = notes_dir / filename
    if note_path.exists():
        print(f"daily note already exists: {filename}")
        return
    
    note_path.write_text(content)
    print(f"created daily note: {filename}")

def process_note(note_name, instruction=None):
    if not note_name:
        print("error: specify note name")
        print("usage: memo process <note.md> [instruction]")
        return
    
    notes_dir = Path("notes")
    note_path = notes_dir / note_name
    
    if not note_path.exists():
        possible_notes = list(notes_dir.glob(f"*{note_name}*"))
        if possible_notes:
            print(f"note not found: {note_name}")
            print("did you mean:")
            for note in possible_notes[:3]:
                print(f"  {note.name}")
        else:
            print(f"note not found: {note_name}")
        return
    
    try:
        content = note_path.read_text()
    except Exception as e:
        print(f"error reading note: {e}")
        return
    
    if instruction:
        try:
            agent = Agent("note-processor")
            result = asyncio.run(agent.run(f"process this note with instruction '{instruction}':\n\n{content}"))
            
            backup_path = notes_dir / f"{note_name}.bak"
            backup_path.write_text(content)
            
            note_path.write_text(result.response)
            print(f"processed: {note_name}")
        except Exception as e:
            print(f"error processing note: {e}")
    else:
        print(content)

def search_notes(query):
    if not query.strip():
        print("error: specify search query")
        print("usage: memo search <query>")
        return
    
    notes_dir = Path("notes")
    if not notes_dir.exists():
        print("no notes found")
        return
    
    notes = list(notes_dir.glob("*.md"))
    if not notes:
        print("no notes found")
        return
    
    print(f"searching {len(notes)} notes for: {query}")
    
    matches = []
    for note in notes:
        try:
            content = note.read_text()
            if query.lower() in content.lower():
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if query.lower() in line.lower():
                        matches.append((note.name, i+1, line.strip()))
                        break
        except Exception:
            continue
    
    if matches:
        print(f"found {len(matches)} matches:")
        for filename, line_num, context in matches:
            print(f"  {filename}:{line_num} - {context[:80]}...")
    else:
        print("no matches found")

def main():
    # Handle help first
    if handle_help_or_empty():
        return
    
    args = sys.argv[1:]
    if not args:
        return list_notes()
    
    cmd = args[0]
    if cmd == "create":
        return create_note(" ".join(args[1:]) if len(args) > 1 else None)
    elif cmd == "list":
        return list_notes()
    elif cmd == "process":
        if len(args) < 2:
            print("❌ error: specify note name")
            print("usage: memo process <note.md> [instruction]")
            return
        return process_note(args[1], " ".join(args[2:]) if len(args) > 2 else None)
    elif cmd == "search":
        return search_notes(" ".join(args[1:]) if len(args) > 1 else "")
    elif cmd == "daily":
        return create_daily_note()
    else:
        # Magic interface - treat as note content
        return create_note(" ".join(args))

if __name__ == "__main__":
    main()