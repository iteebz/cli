#!/usr/bin/env python3
"""cli - interactive helper and menu system"""

import sys
from pathlib import Path

# Tool definitions with enhanced descriptions
TOOLS = {
    "memo": {
        "desc": "notes with ai",
        "detail": "create ai-enhanced notes, daily journals, and search your thoughts",
        "examples": [
            'memo "meeting with team about new feature"',
            'memo daily',
            'memo search "project ideas"'
        ]
    },
    "tasks": {
        "desc": "todos with ai", 
        "detail": "transform simple todos into structured, actionable tasks",
        "examples": [
            'tasks "fix login bug"',
            'tasks todo',
            'tasks prioritize'
        ]
    },
    "goals": {
        "desc": "dreams with ai",
        "detail": "turn vague aspirations into smart, achievable goals",
        "examples": [
            'goals "learn machine learning"',
            'goals review',
            'goals list'
        ]
    },
    "plans": {
        "desc": "strategy with ai",
        "detail": "create strategic plans from daily to monthly timeframes",
        "examples": [
            'plans week "launch new product"',
            'plans day "prepare presentation"',
            'plans review'
        ]
    },
    "research": {
        "desc": "synthesis with ai",
        "detail": "collect sources, synthesize insights, and generate reports",
        "examples": [
            'research "AI trends 2024"',
            'research add https://example.com',
            'research synthesize'
        ]
    },
    "refactor": {
        "desc": "code with ai",
        "detail": "analyze and improve your codebase with ai assistance",
        "examples": [
            'refactor analyze',
            'refactor cleanup myfile.py',
            'refactor modernize src/'
        ]
    },
    "sweep": {
        "desc": "cleanup with ai",
        "detail": "organize and clean up your obsidian vault",
        "examples": [
            'sweep analyze ~/vault',
            'sweep clean ~/vault',
            'sweep duplicates'
        ]
    },
    "manage": {
        "desc": "agents with ai",
        "detail": "Manage and orchestrate AI agents",
        "examples": [
            'manage register agent "description"',
            'manage status',
            'manage list'
        ]
    }
}

def show_banner():
    """Show the main banner"""
    print("╭─────────────────────────────────────╮")
    print("│  🧠 cli - ai tools for scattered minds │")
    print("╰─────────────────────────────────────╯")
    print()

def show_quick_menu():
    """Show a quick interactive menu"""
    show_banner()
    print("✨ Quick Start:")
    print()
    
    for tool, info in TOOLS.items():
        print(f"  {tool:<12} {info['desc']}")
    
    print()
    print("💡 Tips:")
    print("  • Use 'cli help <tool>' for detailed help")
    print("  • Most tools accept natural language: memo \"your idea\"")
    print("  • Use 'cogency <tool>' or just '<tool>' directly")
    print()
    print("🚀 Try: memo \"quick thought\" or tasks \"something to do\"")

def help(tool_name):
    """Show detailed help for a specific tool"""
    if tool_name not in TOOLS:
        print(f"❌ Unknown tool: {tool_name}")
        print(f"Available tools: {', '.join(TOOLS.keys())}")
        return
    
    tool = TOOLS[tool_name]
    print(f"🔧 {tool_name} - {tool['desc']}")
    print("─" * 50)
    print(f"{tool['detail']}")
    print()
    print("📝 Examples:")
    for example in tool['examples']:
        print(f"  {example}")
    print()
    print("💡 Pro tips:")
    
    # Tool-specific tips
    tips = {
        "memo": [
            "Use 'memo daily' for structured daily notes",
            "Search with 'memo search \"keyword\"' to find old notes"
        ],
        "tasks": [
            "AI automatically adds time estimates and difficulty",
            "Use 'tasks prioritize' when feeling overwhelmed"
        ],
        "goals": [
            "AI converts vague ideas into SMART goals",
            "Regular 'goals review' keeps you on track"
        ],
        "plans": [
            "Plans automatically consider your existing goals",
            "Use different timeframes: day, week, month"
        ],
        "research": [
            "Add multiple sources before synthesizing",
            "Ask specific questions with 'research ask \"question\"'"
        ],
        "refactor": [
            "Always creates backups before making changes",
            "Works with multiple programming languages"
        ],
        "sweep": [
            "Designed specifically for Obsidian vaults",
            "Always backs up before cleaning"
        ],
        "manage": [
            "Meta-tool for managing other AI agents",
            "Great for complex multi-step workflows"
        ]
    }
    
    for tip in tips.get(tool_name, []):
        print(f"  • {tip}")

def show_suggestions():
    """Show contextual suggestions based on current directory"""
    cwd = Path.cwd()
    suggestions = []
    
    # Check for common patterns
    if (cwd / "notes").exists():
        suggestions.append("📝 Found notes/ directory - try 'memo list' to see your notes")
    
    if (cwd / "tasks").exists():
        suggestions.append("✅ Found tasks/ directory - try 'tasks todo' to see pending tasks")
    
    if (cwd / "goals").exists():
        suggestions.append("🎯 Found goals/ directory - try 'goals review' for AI analysis")
    
    if any(cwd.glob("*.py")):
        suggestions.append("🐍 Python files detected - try 'refactor analyze' for code insights")
    
    if any(cwd.glob("*.js")) or any(cwd.glob("*.ts")):
        suggestions.append("📜 JavaScript/TypeScript files found - try 'refactor modernize'")
    
    if (cwd / "vault" in str(cwd) or any(cwd.glob("*.md"))):
        suggestions.append("📚 Markdown files detected - try 'sweep analyze' for organization tips")
    
    if suggestions:
        print("🔍 Smart suggestions for this directory:")
        for suggestion in suggestions[:3]:  # Limit to 3 suggestions
            print(f"  {suggestion}")
        print()

def interactive_mode():
    """Simple interactive mode"""
    show_banner()
    print("🎯 Interactive Mode - Type a tool name or 'quit' to exit")
    print()
    
    while True:
        try:
            choice = input("cli> ").strip().lower()
            
            if choice in ['quit', 'exit', 'q']:
                print("👋 Happy productivity!")
                break
            elif choice == '':
                continue
            elif choice in TOOLS:
                help(choice)
                print()
            elif choice == 'help':
                show_quick_menu()
            else:
                print(f"❓ Unknown command: {choice}")
                print("Try: help, <tool-name>, or quit")
        except KeyboardInterrupt:
            print("\n👋 Happy productivity!")
            break

def main():
    """Main CLI helper entry point"""
    args = sys.argv[1:]
    
    if not args:
        show_quick_menu()
        show_suggestions()
        return
    
    cmd = args[0].lower()
    
    if cmd in ['-h', '--help', 'help']:
        if len(args) > 1:
            help(args[1])
        else:
            show_quick_menu()
    elif cmd == 'interactive' or cmd == 'i':
        interactive_mode()
    elif cmd in TOOLS:
        help(cmd)
    else:
        print(f"❌ Unknown command: {cmd}")
        print()
        show_quick_menu()

if __name__ == "__main__":
    main()