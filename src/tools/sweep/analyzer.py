from pathlib import Path
from cogency import Agent

def analyze_vault(vault_path="."):
    """Analyze vault for cleanup opportunities."""
    vault = Path(vault_path)
    if not vault.exists():
        print(f"vault not found: {vault_path}")
        return
    
    notes = list(vault.glob("**/*.md"))
    if not notes:
        print("no markdown files found")
        return
    
    print(f"analyzing {len(notes)} notes in {vault_path}")
    
    # Sample first few notes for analysis
    sample_content = ""
    for note in notes[:5]:
        try:
            content = note.read_text(encoding='utf-8', errors='ignore')
            sample_content += f"=== {note.name} ===\n{content[:300]}...\n\n"
        except Exception:
            continue
    
    try:
        agent = Agent("vault-cleaner")
        result = agent.run(f"""Analyze these Obsidian notes for cleanup opportunities:

{sample_content}

Identify:
- Formatting inconsistencies
- Duplicate content patterns  
- Organizational issues
- Broken links
- Cleanup suggestions""")
        
        print(result.response)
    except Exception as e:
        print(f"error analyzing vault: {e}")