from pathlib import Path
from cogency import Agent

def organize_vault(vault_path="."):
    """Get organization recommendations for vault."""
    vault = Path(vault_path)
    notes = list(vault.glob("**/*.md"))
    
    if not notes:
        print("no markdown files found")
        return
    
    print(f"analyzing organization for {len(notes)} notes...")
    
    # Sample content for organization analysis
    sample_content = ""
    for note in notes[:10]:
        try:
            content = note.read_text(encoding='utf-8', errors='ignore')
            sample_content += f"=== {note.name} ===\n{content[:200]}...\n\n"
        except Exception:
            continue
    
    try:
        agent = Agent("vault-cleaner")
        result = agent.run(f"""Suggest folder organization for this Obsidian vault:

{sample_content}

Recommend:
- Folder structure
- Categorization strategy
- File naming improvements""")
        
        print(result.response)
    except Exception as e:
        print(f"error analyzing organization: {e}")