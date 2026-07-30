# AI Agent Setup Guide

This is a basic setup for creating an AI agent using the Claude API.

## Prerequisites

- Python 3.8+
- Claude API key (get one from [console.anthropic.com](https://console.anthropic.com/))

## Setup Instructions

1. **Clone the repository and set up the environment:**
   ```bash
   git clone <repo>
   cd <repo-folder>  # replace with the cloned repository folder name

   # Create and activate virtual environment (macOS/Linux)
   python -m venv .venv
   source .venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**
   - Copy `.env` to `.env`
   - Add your Claude API key to the `.env` file:
   ```bash
   cp .env .env
   ```
   - Edit `.env` and replace `your_api_key_here` with your actual API key

5. **Run the agent:**
   ```bash
   python main.py
   ```

## How It Works

The agent maintains a conversation history and can:
- Remember previous messages in a conversation
- Respond contextually to follow-up questions
- Handle multiple user inputs in a session

## Project Structure

```
.
├── main.py              # Main agent script
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .env                # Your local API configuration (add to .gitignore)
└── README.md           # This file
```

## Example Usage

```
🤖 AI Agent initialized. Type 'exit' to quit.

You: What is the capital of France?
Agent: The capital of France is Paris. It's located in the north-central part of the country and is one of the most famous cities in the world, known for landmarks like the Eiffel Tower, the Louvre Museum, and Notre-Dame Cathedral.

You: Tell me more about it
Agent: [Agent responds with more information about Paris...]

You: exit
Goodbye!
```

## Security Notes

- **Never commit `.env` file** to version control
- Keep your API key secure and never share it
- Use `.env` file for local development only

## Customization

You can customize the agent by modifying:
- **System prompt** in `create_agent()` function to change agent behavior
- **Model** in `chat()` function to use different Claude models
- **max_tokens** to adjust response length

## Troubleshooting

- **ImportError for anthropic**: Run `pip install -r requirements.txt`
- **API key not found**: Ensure `.env` file exists and has `ANTHROPIC_API_KEY`
- **Connection errors**: Check your internet connection and API key validity
