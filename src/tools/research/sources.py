"""sources - research source management"""

import asyncio
from pathlib import Path
from cogency import Agent
from .session import get_session, save_session

def add_source(source):
    session = get_session()
    if not session.get("topic"):
        print("no research session. start with: research <topic>")
        return
    
    print(f"analyzing: {source}")
    
    try:
        agent = Agent("research-assistant")
        
        if source.startswith(("http://", "https://")):
            result = asyncio.run(agent.run(f"research this URL for insights on '{session['topic']}': {source}"))
        elif Path(source).exists():
            content = Path(source).read_text()[:2000]
            result = asyncio.run(agent.run(f"analyze this document for insights on '{session['topic']}':\n\n{content}"))
        else:
            print(f"source not found: {source}")
            return
        
        session["sources"].append({"source": source, "insights": result.response})
        save_session(session)
        print("source added")
        
    except Exception as e:
        print(f"error: {e}")

def list_sources():
    session = get_session()
    sources = session.get("sources", [])
    
    if not sources:
        print("no sources")
        return
    
    print(f"{len(sources)} sources:")
    for i, source in enumerate(sources, 1):
        print(f"  {i}. {source['source']}")