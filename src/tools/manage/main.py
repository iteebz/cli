#!/usr/bin/env python3
"""manage - agents with ai"""

import json
import asyncio
from pathlib import Path
from datetime import datetime
from cogency import Agent
from src.shared.cli import run_cli

def get_registry_path():
    return Path.home() / ".cogency" / "agents.json"

def load_registry():
    registry_path = get_registry_path()
    if not registry_path.exists():
        return {}
    
    try:
        return json.loads(registry_path.read_text())
    except Exception:
        return {}

def save_registry(registry):
    registry_path = get_registry_path()
    registry_path.parent.mkdir(exist_ok=True)
    registry_path.write_text(json.dumps(registry, indent=2))

def list_agents(args=None):
    registry = load_registry()
    if not registry:
        print("no agents")
        return
    
    print(f"agents ({len(registry)}):")
    for name, config in registry.items():
        created = config.get("created", "unknown")[:10]
        desc = config.get("description", "no description")
        print(f"  {name} - {desc} ({created})")

def register_agent(args):
    if not args:
        print("usage: manage register <name> [description]")
        return
    
    name = args[0]
    description = " ".join(args[1:]) if len(args) > 1 else f"agent: {name}"
    
    registry = load_registry()
    
    if name in registry:
        print(f"exists: {name}")
        return
    
    config = {
        "name": name,
        "description": description,
        "created": datetime.now().isoformat(),
        "status": "active"
    }
    
    registry[name] = config
    save_registry(registry)
    print(f"registered: {name}")

def remove_agent(args):
    if not args:
        print("usage: manage remove <name>")
        return
    
    name = args[0]
    registry = load_registry()
    
    if name not in registry:
        print(f"not found: {name}")
        return
    
    del registry[name]
    save_registry(registry)
    print(f"removed: {name}")

def status_agents(args=None):
    registry = load_registry()
    if not registry:
        print("no agents")
        return
    
    print("status:")
    for name, config in registry.items():
        print(f"  {name}: active")

def test_agent(args):
    if not args:
        print("usage: manage test <name>")
        return
    
    name = args[0]
    
    try:
        agent = Agent(name)
        result = asyncio.run(agent.run("test message"))
        print(f"test {name}: ok")
        print(result.response[:100] + "..." if len(result.response) > 100 else result.response)
    except Exception as e:
        print(f"test {name}: error - {e}")

commands = {
    "list": list_agents,
    "register": register_agent,
    "remove": remove_agent,
    "status": status_agents,
    "test": test_agent
}

def main():
    run_cli("manage", commands, list_agents)

if __name__ == "__main__":
    main()