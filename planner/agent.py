from google.adk.agents.llm_agent import Agent

planner_agent = Agent(
    model='gemini-2.5-flash',
    name='planner_agent',
    description='Creates a study plan and calendar events.',
    instruction='''You are a meticulous study planner.
Given a list of recommended resources and the user's goals:
1. Create a structured study roadmap (e.g., Week 1, Week 2, etc, or Module 1, Module 2).
2. Assign specific resources to each time block.
3. Suggest specific calendar events (e.g., "Watch Course X Module 1", "Complete Project Y").
4. Format the output as a clear, actionable plan.
'''
)
