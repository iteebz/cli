from pathlib import Path
from cogency import Agent

def format_vault(vault_path="."):
    """Format notes with consistent markdown style."""
    vault = Path(vault_path)
    notes = list(vault.glob("**/*.md"))
    
    if not notes:
        print("no markdown files found")
        return
    
    print(f"formatting {len(notes)} notes...")
    
    try:
        agent = Agent("markdown-formatter")
        formatted_count = 0
        
        for note in notes:
            try:
                content = note.read_text(encoding='utf-8', errors='ignore')
                
                if len(content.strip()) < 20:
                    continue
                    
                result = agent.run(f"""Format this markdown note with consistent style:
- Proper heading hierarchy
- Consistent list formatting  
- Clean spacing
- Preserve Obsidian links and syntax

{content}""")
                
                if result.response.strip() != content.strip():
                    # Backup and update
                    backup_path = note.with_suffix('.md.bak')
                    backup_path.write_text(content)
                    note.write_text(result.response)
                    
                    formatted_count += 1
                    print(f"formatted: {note.name}")
                    
            except Exception as e:
                print(f"error formatting {note.name}: {e}")
        
        print(f"formatted {formatted_count} notes (originals backed up)")
        
    except Exception as e:
        print(f"error initializing formatter: {e}")