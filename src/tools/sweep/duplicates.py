from pathlib import Path

def find_duplicates(vault_path="."):
    """Find duplicate notes in vault."""
    vault = Path(vault_path)
    notes = list(vault.glob("**/*.md"))
    
    if not notes:
        print("no markdown files found")
        return
    
    print(f"checking {len(notes)} notes for duplicates...")
    
    content_hashes = {}
    duplicates = []
    
    for note in notes:
        try:
            content = note.read_text(encoding='utf-8', errors='ignore')
            content_hash = hash(content.strip())
            
            if content_hash in content_hashes:
                duplicates.append((note, content_hashes[content_hash]))
            else:
                content_hashes[content_hash] = note
        except Exception:
            continue
    
    if duplicates:
        print(f"found {len(duplicates)} potential duplicates:")
        for dup, original in duplicates:
            print(f"  {dup.name} → {original.name}")
    else:
        print("no exact duplicates found")