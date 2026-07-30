import os
from dotenv import load_dotenv
from anthropic import Anthropic

import config

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)


def create_agent():
    """Create and return a basic AI agent with conversation history."""
    return {
        "conversation_history": [],
        "system_prompt": getattr(config, "SYSTEM_PROMPT", "You are a helpful AI assistant.")
    }

def extract_text(response):
    return "".join(
        block.text
        for block in response.content
        if block.type == "text"
    )


def chat(agent, user_message):
    """Send a message to the agent and get a response."""
    # Add user message to conversation history
    agent["conversation_history"].append({
        "role": "user",
        "content": user_message
    })
    
    # Create a message with the Anthropic API
    response = client.messages.create(
        model=config.ANTHROPIC_MODEL,
        max_tokens=config.ANTHROPIC_MAX_TOKENS,
        system=agent["system_prompt"],
        messages=agent["conversation_history"]
    )
    
    # Extract the assistant's response
    assistant_message = extract_text(response)

    # Add assistant response to conversation history
    agent["conversation_history"].append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def main():
    """Main function to run the AI agent in a chat loop."""
    print("🤖 AI Agent initialized. Type 'exit' to quit.\n")
    
    # Create the agent
    agent = create_agent()
    
    # Chat loop
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = chat(agent, user_input)
            print(f"\nAgent: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
