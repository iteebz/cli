#!/usr/bin/env python3
"""refactor - code with ai"""

import asyncio
from pathlib import Path
from cogency import Agent
from src.shared.cli import run_cli

def get_code_files(path):
    target = Path(path)
    if not target.exists():
        return []
    
    extensions = ['*.py', '*.js', '*.ts', '*.jsx', '*.tsx']
    
    if target.is_file():
        return [target] if any(target.match(ext) for ext in extensions) else []
    
    files = []
    for ext in extensions:
        files.extend(target.glob(f"**/{ext}"))
    return files

def analyze_code(args):
    path = args[0] if args else "."
    
    files = get_code_files(path)
    if not files:
        print("no code files")
        return
    
    print(f"analyzing {len(files)} files...")
    
    content = ""
    for file in files[:3]:
        try:
            text = file.read_text(encoding='utf-8', errors='ignore')
            content += f"=== {file.name} ===\n{text[:600]}\n\n"
        except Exception:
            continue
    
    if not content:
        print("no readable files")
        return
    
    try:
        agent = Agent("code-analyzer")
        result = asyncio.run(agent.run(f"analyze this code for improvements:\n{content}"))
        print(result.response)
    except Exception as e:
        print(f"error: {e}")

def cleanup_file(args):
    if not args:
        print("usage: refactor cleanup <file>")
        return
    
    file_path = Path(args[0])
    if not file_path.exists():
        print(f"not found: {args[0]}")
        return
    
    try:
        content = file_path.read_text()
        
        agent = Agent("code-cleaner")
        result = asyncio.run(agent.run(f"clean up this code:\n\n{content}"))
        
        backup_path = file_path.with_suffix(file_path.suffix + '.bak')
        backup_path.write_text(content)
        file_path.write_text(result.response)
        
        print(f"cleaned: {file_path.name}")
        print(f"backup: {backup_path.name}")
        
    except Exception as e:
        print(f"error: {e}")

def modernize_code(args):
    path = args[0] if args else "."
    
    files = get_code_files(path)
    if not files:
        print("no code files")
        return
    
    print(f"modernizing {len(files)} files...")
    
    content = ""
    for file in files[:2]:
        try:
            text = file.read_text()
            content += f"=== {file.name} ===\n{text[:500]}\n\n"
        except Exception:
            continue
    
    try:
        agent = Agent("code-modernizer")
        result = asyncio.run(agent.run(f"suggest modernization for:\n{content}"))
        print(result.response)
    except Exception as e:
        print(f"error: {e}")

commands = {
    "analyze": analyze_code,
    "cleanup": cleanup_file,
    "modernize": modernize_code
}

def main():
    run_cli("refactor", commands, analyze_code)

if __name__ == "__main__":
    main()