import asyncio
import os
import sys
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from agent import root_agent
from google.genai import types

async def main():
    service = InMemorySessionService()
    # Create the session with required app_name
    session = await service.create_session(user_id="user1", app_name="multi_agent_app")
    
    # Use prompt from command line or default
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = "Generative AI alanında kendimi nasıl geliştirebilirim?"
        
    print(f"🔹 User Input: {prompt}\n")
    print("🔹 Running Root Agent Orchestrator...\n")
    
    runner = Runner(agent=root_agent, session_service=service, app_name="multi_agent_app")
    
    content = types.Content(role="user", parts=[types.Part(text=prompt)])
    
    try:
        async for event in runner.run_async(new_message=content, session_id=session.id, user_id="user1"):
            # Try to print text from event if available, handling different event structures
            text_chunk = ""
            if hasattr(event, 'text') and event.text:
                 text_chunk = event.text
            elif hasattr(event, 'content'):
                 if isinstance(event.content, list):
                     for part in event.content:
                         if hasattr(part, 'text') and part.text:
                             text_chunk += part.text
                 elif hasattr(event.content, 'parts'): 
                     for part in event.content.parts:
                         if hasattr(part, 'text') and part.text:
                             text_chunk += part.text
                 else:
                     # Fallback string representation might be noisy but useful for debug
                     pass 
            
            if text_chunk:
                print(text_chunk, end="", flush=True)
                
    except Exception as e:
        print(f"\nError during execution: {e}")

    print("\n\n✅ Orchestration completed.")

if __name__ == "__main__":
    if "GOOGLE_API_KEY" not in os.environ:
        print("⚠️  WARNING: GOOGLE_API_KEY environment variable is not set. The agent will likely fail.")
        print("Export it using: export GOOGLE_API_KEY='your_key'")
    
    asyncio.run(main())
