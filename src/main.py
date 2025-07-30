#!/usr/bin/env python3
"""cli - ai tools for scattered minds"""

import sys

tools = {
    "memo": "notes with ai",
    "tasks": "todos with ai", 
    "goals": "dreams with ai",
    "plans": "strategy with ai",
    "research": "synthesis with ai",
    "refactor": "code with ai",
    "sweep": "cleanup with ai",
    "manage": "agents with ai"
}

def show_help():
    print("╭───────────────────────────────────────╮")
    print("│  🧠 cli ai tools for scattered minds  │")
    print("╰───────────────────────────────────────╯")
    print()
    print("✨ Usage:")
    print("  cli <tool> [args...]")
    print()
    print("🔧 Tools:")
    for tool, desc in tools.items():
        print(f"  {tool:<12} {desc}")
    print()
    print("📝 Examples:")
    print("  cli memo \"meeting notes\"")
    print("  cli tasks \"fix bug\"")
    print("  cli goals \"learn rust\"")
    print()
    print("💡 Pro Tips:")
    print("  • Use 'cli' for interactive help and menu")
    print("  • Use '<tool> --help' for detailed tool help")
    print("  • Most tools accept natural language input")
    print()
    print("🚀 chaos → clarity")

def run_tool(tool_name, args):
    if tool_name not in tools:
        print(f"❌ Unknown tool: {tool_name}")
        print(f"📋 Available: {', '.join(tools.keys())}")
        print(f"💡 Try: 'cli help {tool_name}' or 'cli' for interactive menu")
        return 1
    
    try:
        module_path = f"src.tools.{tool_name}.main"
        module = __import__(module_path, fromlist=['main'])
        
        original_argv = sys.argv
        sys.argv = [tool_name] + args
        
        try:
            return module.main()
        finally:
            sys.argv = original_argv
            
    except ImportError as e:
        print(f"❌ Error loading {tool_name}: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error running {tool_name}: {e}")
        return 1

def main():
    args = sys.argv[1:]
    
    if not args or args[0] in ["-h", "--help", "help"]:
        show_help()
        return 0
    
    return run_tool(args[0], args[1:])

if __name__ == "__main__":
    sys.exit(main())