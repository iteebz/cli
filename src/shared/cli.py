"""cli - shared minimal patterns"""
import sys

def run_cli(tool_name, commands, default_cmd=None):
    """ultra-minimal cli runner"""
    args = sys.argv[1:]
    
    if not args:
        if default_cmd:
            # show simple ux description instead of help ceremony
            return default_cmd([])
        else:
            print(f"usage: {tool_name} [command]")
            print(f"commands: {', '.join(commands.keys())}")
            return 0
    
    if args[0] in ["-h", "--help", "help"]:
        print(f"usage: {tool_name} [command]")
        print(f"commands: {', '.join(commands.keys())}")
        return 0
    
    cmd = args[0] 
    if cmd in commands:
        return commands[cmd](args[1:])
    elif default_cmd:
        return default_cmd(args)
    else:
        print(f"unknown: {cmd}")
        return 1

def print_items(items, item_type):
    """print items consistently"""
    if not items:
        print(f"no {item_type}")
        return
    
    print(f"{item_type} ({len(items)}):")
    for item in items:
        item_id = item.get("id", "unknown")
        short_id = item_id[:8] if len(item_id) > 8 else item_id
        status = item.get("status", "unknown")
        created = item.get("created", "unknown")[:10]
        
        if "priority" in item:
            priority = item.get("priority", "medium")
            icon = {"high": "🔥", "medium": "📋", "low": "📝"}.get(priority, "📋")
            print(f"  {icon} {short_id} - {status} ({created})")
        else:
            print(f"  {short_id} - {status} ({created})")