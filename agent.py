import os
from anthropic import Anthropic

class Agent:
    def __init__(self, system_prompt, model, max_tokens):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.conversation_history = []
        self.system_prompt = system_prompt
        self.model = model
        self.max_tokens = max_tokens

    def chat(self, user_message):
        if not user_message or not user_message.strip():
            raise ValueError("User message cannot be empty.")

        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self.conversation_history
        )

        assistant_message = self._extract_text(response.content)

        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    @staticmethod
    def _extract_text(content):
        return " ".join(
            block.text
            for block in content
            if hasattr(block, "text")
        )

    def get_history(self):
        return self.conversation_history.copy()

    def clear_history(self):
        self.conversation_history = []
