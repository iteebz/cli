from pathlib import Path
from cogency import Agent

def clean_vault(vault_path="."):
    """Clean up notes with AI assistance."""
    vault = Path(vault_path)
    notes = list(vault.glob("**/*.md"))
    
    if not notes:
        print("no markdown files found")
        return
    
    print(f"cleaning {len(notes)} notes...")
    
    try:
        agent = Agent("vault-cleaner")
        cleaned_count = 0
        
        for note in notes:
            try:
                content = note.read_text(encoding='utf-8', errors='ignore')
                
                if len(content.strip()) < 50:
                    continue
                    
                result = agent.run(f"""Clean up this Obsidian note:
- Fix markdown formatting
- Improve structure and readability  
- Preserve all content and links
- Maintain Obsidian syntax

{content}""")
                
                # Backup and update
                backup_path = note.with_suffix('.md.bak')
                backup_path.write_text(content)
                note.write_text(result.response)
                
                cleaned_count += 1
                print(f"cleaned: {note.name}")
                
            except Exception as e:
                print(f"error cleaning {note.name}: {e}")
        
        print(f"cleaned {cleaned_count} notes (originals backed up)")
        
    except Exception as e:
        print(f"error initializing cleaner: {e}")