"""storage - filesystem utilities"""
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

class Storage:
    """Simple JSON-based storage for CLI tools"""
    
    def __init__(self, data_type: str):
        self.data_type = data_type
        # centralized data directory - single source of truth
        base_dir = Path.home() / ".cli"
        self.data_dir = base_dir / data_type
    
    def save(self, item: Dict) -> None:
        """Save item to filesystem"""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        item_id = item["id"]
        item_file = self.data_dir / f"{item_id}.json"
        item_file.write_text(json.dumps(item, indent=2))
    
    def load_all(self) -> List[Dict]:
        """Load all items from filesystem"""
        if not self.data_dir.exists():
            return []
        
        items = []
        for item_file in self.data_dir.glob("*.json"):
            try:
                item_data = json.loads(item_file.read_text())
                items.append(item_data)
            except Exception:
                continue
        
        return sorted(items, key=lambda i: i.get("created", ""))
    
    def load_one(self, item_id: str) -> Optional[Dict]:
        """Load single item by ID"""
        item_file = self.data_dir / f"{item_id}.json"
        if not item_file.exists():
            return None
        
        try:
            return json.loads(item_file.read_text())
        except Exception:
            return None
    
    def update(self, item_id: str, updates: Dict) -> bool:
        """Update existing item"""
        item = self.load_one(item_id)
        if not item:
            return False
        
        item.update(updates)
        item["updated"] = datetime.now().isoformat()
        self.save(item)
        return True
    
    def delete(self, item_id: str) -> bool:
        """Delete item"""
        item_file = self.data_dir / f"{item_id}.json"
        if not item_file.exists():
            return False
        
        try:
            item_file.unlink()
            return True
        except Exception:
            return False

def generate_id(prefix: str = "") -> str:
    """Generate timestamped ID"""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{prefix}-{timestamp}" if prefix else timestamp

def find_by_short_id(storage_instance, short_id: str):
    """Find item by short ID (first few chars)"""
    items = storage_instance.load_all()
    matches = [item for item in items if item["id"].startswith(short_id)]
    
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        return None  # ambiguous
    else:
        return None  # not found

def create_item(data_type: str, description: str, **kwargs) -> Dict:
    """Create a new item with standard fields"""
    item_id = generate_id(kwargs.get("prefix", ""))
    return {
        "id": item_id,
        "created": datetime.now().isoformat(),
        "description": description,
        **kwargs
    }