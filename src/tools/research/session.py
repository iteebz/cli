"""session - research session management"""

import json
from pathlib import Path

def get_session():
    research_dir = Path("research")
    research_dir.mkdir(exist_ok=True)
    session_file = research_dir / "session.json"
    
    if session_file.exists():
        try:
            return json.loads(session_file.read_text())
        except Exception:
            pass
    return {}

def save_session(session):
    research_dir = Path("research")
    research_dir.mkdir(exist_ok=True)
    session_file = research_dir / "session.json"
    session_file.write_text(json.dumps(session, indent=2))