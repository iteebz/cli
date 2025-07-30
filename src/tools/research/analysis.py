"""analysis - research synthesis"""

import asyncio
from cogency import Agent
from .session import get_session

def synthesize_research():
    session = get_session()
    sources = session.get("sources", [])
    
    if not sources:
        print("no sources to synthesize")
        return
    
    print(f"synthesizing {len(sources)} sources...")
    
    all_insights = "\n\n".join([f"Source: {s['source']}\nInsights: {s['insights']}" for s in sources])
    
    try:
        agent = Agent("research-assistant")
        result = asyncio.run(agent.run(f"synthesize research on '{session['topic']}' from these sources:\n\n{all_insights}"))
        print(result.response)
    except Exception as e:
        print(f"error: {e}")

def ask_question(question):
    if not question.strip():
        print("usage: research ask \"your question\"")
        return
    
    session = get_session()
    sources = session.get("sources", [])
    
    if not sources:
        print("no sources available")
        return
    
    print(f"researching: {question}")
    
    all_insights = "\n\n".join([f"Source: {s['source']}\nInsights: {s['insights']}" for s in sources])
    
    try:
        agent = Agent("research-assistant")
        result = asyncio.run(agent.run(f"answer this question about '{session['topic']}': {question}\n\nBased on:\n{all_insights}"))
        print(result.response)
    except Exception as e:
        print(f"error: {e}")