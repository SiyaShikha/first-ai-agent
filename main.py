from dotenv import load_dotenv
from agent import Agent
import config
from prompts import BASE_PROMPT

load_dotenv()

def main():
    print("🤖 AI Agent initialized. Type 'exit' to quit.\n")

    model = getattr(config, "ANTHROPIC_MODEL", "claude-sonnet-5")
    max_tokens = getattr(config, "ANTHROPIC_MAX_TOKENS", 1000)
    agent = Agent(system_prompt=BASE_PROMPT, model=model, max_tokens=max_tokens)

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = agent.chat(user_input)
            print(f"\nAgent: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()

