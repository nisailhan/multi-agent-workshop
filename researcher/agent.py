from google.adk.agents.llm_agent import Agent

researcher_agent = Agent(
    model='gemini-2.5-flash',
    name='researcher_agent',
    description='Searches for educational resources.',
    instruction='''You are a specialized research assistant for educational resources.
Given a User Profile and Learning Goal, search for and identify the best courses, tutorials, and materials.
Focus on reputable platforms like Coursera, EdX, Kaggle, Udacity, and high-quality YouTube channels.
Prioritize highly-rated and recent content.
For each recommendation, provide:
- Title
- Platform/Source
- Brief description of why it fits the user's goal.
- Estimated duration.
'''
)
