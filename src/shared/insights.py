"""insights - ai-powered insights"""
import asyncio
from cogency import Agent
from typing import Dict, List, Optional

class Insights:
    """Generate AI insights for productivity items"""
    
    @staticmethod
    def generate_insight(agent_name: str, item_type: str, description: str, context: str = "") -> str:
        """Generate AI insight for any item type"""
        try:
            agent = Agent(agent_name)
            prompt = f"Provide insights for this {item_type}: {description}"
            if context:
                prompt += f"\n\nContext:\n{context}"
            
            result = asyncio.run(agent.run(prompt))
            return result.response
        except Exception as e:
            return f"Insight generation failed: {e}"
    
    @staticmethod
    def analyze_collection(agent_name: str, items: List[Dict], analysis_type: str) -> str:
        """Analyze collection of items with AI"""
        if not items:
            return f"No items to analyze for {analysis_type}"
        
        try:
            items_summary = "\n".join([
                f"{item.get('id', 'unknown')}: {item.get('description', '')[:100]}..."
                for item in items
            ])
            
            agent = Agent(agent_name)
            result = asyncio.run(agent.run(f"Analyze these items for {analysis_type}:\n\n{items_summary}"))
            return result.response
        except Exception as e:
            return f"Analysis failed: {e}"
    
    @staticmethod
    def goal_insights(description: str) -> str:
        """Generate SMART goal insights"""
        return Insights.generate_insight(
            "goal-setter", 
            "goal", 
            description,
            "Make it SMART (Specific, Measurable, Achievable, Relevant, Time-bound)"
        )
    
    @staticmethod
    def plan_insights(description: str, timeframe: str, goals_context: str = "") -> str:
        """Generate strategic plan insights"""
        context = f"Timeframe: {timeframe}"
        if goals_context:
            context += f"\n\nExisting goals:\n{goals_context}"
        
        return Insights.generate_insight(
            "strategic-planner",
            f"{timeframe} plan",
            description,
            context
        )
    
    @staticmethod
    def task_insights(description: str) -> str:
        """Generate task structure and detail insights"""
        return Insights.generate_insight(
            "task-enhancer",
            "task",
            description,
            "Include time estimate, difficulty, prerequisites, and success criteria"
        )
    
    @staticmethod
    def prioritization_insights(tasks: List[Dict]) -> str:
        """Generate task prioritization insights"""
        return Insights.analyze_collection(
            "task-prioritizer",
            tasks,
            "priority and sequencing recommendations"
        )