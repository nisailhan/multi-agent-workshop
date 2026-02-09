import asyncio
import sys
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from analyst.agent import analyst_agent
from researcher.agent import researcher_agent
from planner.agent import planner_agent

async def get_response(agent, prompt, session_service):
    """Run an agent and aggregate the response text."""
    # Create a runner for this specific agent
    runner = Runner(agent=agent, session_service=session_service, app_name="multi_agent_app")
    full_response = ""
    session = await session_service.create_session(user_id="user1", app_name="multi_agent_app")
    from google.genai import types
    content = types.Content(role="user", parts=[types.Part(text=prompt)])
    async for event in runner.run_async(new_message=content, session_id=session.id, user_id="user1"):
        # We accumulate text from events. 
        # The structure of event depends on ADK version, but converting to str usually gives something useful if text attribute is missing.
        # Common attributes: text, content, chunks.
        if hasattr(event, 'text') and event.text:
            full_response += event.text
        elif hasattr(event, 'content'):
             # If content is a list of parts, join them
             if isinstance(event.content, list):
                 for part in event.content:
                     if hasattr(part, 'text'):
                         full_response += part.text
                     else:
                         full_response += str(part)
             else:
                 full_response += str(event.content)
        
    return full_response

async def main():
    # Use a single session service (though we rely on explicit prompt passing here)
    service = InMemorySessionService()
    
    # Get user input
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        # Default prompt for demonstration if no arg provided
        print("No input provided. Using default demo question.")
        user_input = "Generative AI alanında kendimi nasıl geliştirebilirim?"
        
    print(f"\n🔹 User Input: {user_input}\n")

    # Step 1: Analyst
    print("🔹 Agent 1: Analyst (Analyzing background and goals)...")
    try:
        analyst_out = await get_response(analyst_agent, user_input, service)
        print(f"--- Analyst Output ---\n{analyst_out}\n")
    except Exception as e:
        print(f"Analyst failed: {e}")
        import traceback
        traceback.print_exc()
        return

    # Step 2: Researcher
    print("🔹 Agent 2: Researcher (Finding resources)...")
    try:
        researcher_prompt = f"Based on this analysis, find resources:\n{analyst_out}"
        researcher_out = await get_response(researcher_agent, researcher_prompt, service)
        print(f"--- Researcher Output ---\n{researcher_out}\n")
    except Exception as e:
        print(f"Researcher failed: {e}")
        import traceback
        traceback.print_exc()
        return

    # Step 3: Planner
    print("🔹 Agent 3: Planner (Creating schedule)...")
    try:
        planner_prompt = f"Create a study plan for:\n{researcher_out}\nUser Goal Summary: {analyst_out}"
        planner_out = await get_response(planner_agent, planner_prompt, service)
        print(f"--- Planner Output ---\n{planner_out}\n")
    except Exception as e:
        print(f"Planner failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("✅ workflow completed successfully.")

if __name__ == "__main__":
    asyncio.run(main())
