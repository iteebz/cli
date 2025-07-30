#!/usr/bin/env python3
"""sweep - cleanup with ai"""

import asyncio
from pathlib import Path
from cogency import Agent
from src.shared.cli import run_cli

def get_md_files(path):
    target = Path(path)
    if not target.exists():
        return []
    
    if target.is_file() and target.suffix == '.md':
        return [target]
    
    return list(target.glob("**/*.md"))

def analyze_vault(args):
    path = args[0] if args else "."
    
    files = get_md_files(path)
    if not files:
        print("no markdown files")
        return
    
    print(f"analyzing {len(files)} files...")
    
    sample_content = ""
    for file in files[:5]:
        try:
            content = file.read_text()[:300]
            sample_content += f"=== {file.name} ===\n{content}\n\n"
        except Exception:
            continue
    
    try:
        agent = Agent("vault-analyzer")
        result = asyncio.run(agent.run(f"analyze this obsidian vault for organization issues:\n{sample_content}"))
        print(result.response)
    except Exception as e:
        print(f"error: {e}")

def clean_vault(args):
    path = args[0] if args else "."
    
    files = get_md_files(path)
    if not files:
        print("no markdown files")
        return
    
    print(f"cleaning {len(files)} files...")
    cleaned = 0
    
    for file in files:
        try:
            content = file.read_text()
            agent = Agent("vault-cleaner")
            result = asyncio.run(agent.run(f"clean up this markdown file:\n{content}"))
            
            if result.response != content:
                backup = file.with_suffix('.md.bak')
                backup.write_text(content)
                file.write_text(result.response)
                cleaned += 1
                
        except Exception as e:
            print(f"error cleaning {file.name}: {e}")
            continue
    
    print(f"cleaned {cleaned} files")

def find_duplicates(args):
    path = args[0] if args else "."
    
    files = get_md_files(path)
    if not files:
        print("no markdown files")
        return
    
    print(f"checking {len(files)} files for duplicates...")
    
    content_map = {}
    for file in files:
        try:
            content = file.read_text().strip()
            if content in content_map:
                print(f"duplicate: {file.name} == {content_map[content].name}")
            else:
                content_map[content] = file
        except Exception:
            continue

def organize_vault(args):
    path = args[0] if args else "."
    
    files = get_md_files(path)
    if not files:
        print("no markdown files")
        return
    
    print(f"organizing {len(files)} files...")
    
    file_list = "\n".join([f.name for f in files[:20]])
    
    try:
        agent = Agent("vault-organizer")
        result = asyncio.run(agent.run(f"suggest organization for these files:\n{file_list}"))
        print(result.response)
    except Exception as e:
        print(f"error: {e}")

commands = {
    "analyze": analyze_vault,
    "clean": clean_vault,
    "duplicates": find_duplicates,
    "organize": organize_vault
}

def main():
    run_cli("sweep", commands, analyze_vault)

if __name__ == "__main__":
    main()