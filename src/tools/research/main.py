#!/usr/bin/env python3
"""research - synthesis with ai"""

from pathlib import Path
from src.shared.cli import run_cli
from .session import get_session, save_session
from .sources import add_source, list_sources
from .analysis import synthesize_research, ask_question
from .export import export_research

def start_research(args):
    if not args:
        print("usage: research \"topic\"")
        return
    
    topic = " ".join(args)
    session = {"topic": topic, "sources": []}
    save_session(session)
    print(f"started: {topic}")

def show_status(args=None):
    session = get_session()
    if not session.get("topic"):
        print("no session")
        print("start with: research \"topic\"")
        return
    
    print(f"topic: {session['topic']}")
    print(f"sources: {len(session.get('sources', []))}")

def add_source_cmd(args):
    if not args:
        print("usage: research add <url|file>")
        return
    return add_source(args[0])

def ask_cmd(args):
    return ask_question(" ".join(args))

def export_cmd(args):
    return export_research(args[0] if args else None)

def clear_session(args=None):
    response = input("clear session? (y/N): ").strip().lower()
    if response in ['y', 'yes']:
        research_dir = Path("research")
        session_file = research_dir / "session.json"
        if session_file.exists():
            session_file.unlink()
        print("cleared")

commands = {
    "add": add_source_cmd,
    "synthesize": lambda args: synthesize_research(),
    "ask": ask_cmd,
    "export": export_cmd,
    "list": lambda args: list_sources(),
    "clear": clear_session,
    "status": show_status
}

def main():
    run_cli("research", commands, start_research)

if __name__ == "__main__":
    main()