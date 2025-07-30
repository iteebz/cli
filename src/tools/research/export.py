"""export - research report generation"""

from pathlib import Path
from datetime import datetime
from .session import get_session

def export_research(filename=None):
    session = get_session()
    
    if not session.get("topic"):
        print("no research session to export")
        return
    
    if not filename:
        topic_slug = "-".join(session["topic"].lower().split()[:3])
        topic_slug = "".join(c for c in topic_slug if c.isalnum() or c in "-")
        filename = f"research-{topic_slug}-{datetime.now().strftime('%Y%m%d')}.md"
    
    # Build report
    report = f"# Research: {session['topic']}\n\n"
    
    sources = session.get("sources", [])
    if sources:
        for i, source in enumerate(sources, 1):
            report += f"## Source {i}: {source['source']}\n\n"
            report += source["insights"] + "\n\n"
    
    # Write report
    research_dir = Path("research")
    report_path = research_dir / filename
    report_path.write_text(report)
    
    print(f"exported: {filename} ({len(sources)} sources)")