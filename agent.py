import os
import re
from anthropic import Anthropic
from tools.registry import TOOL_MAP


class Agent:
    def __init__(self, system_prompt: str, model: str, max_tokens: int):
        api_key = os.getenv("ANTHROPIC_API_KEY")

        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY is not configured.")

        self.client = Anthropic(api_key=api_key)
        self.system_prompt = system_prompt
        self.model = model
        self.max_tokens = max_tokens
        self.conversation_history = []

    def chat(self, user_message: str) -> str:
        self.conversation_history.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        while True:
            assistant_message = self._call_llm()
            action = self._parse_action(assistant_message)

            if action is None:
                self.conversation_history.append(
                    {
                        "role": "assistant",
                        "content": assistant_message,
                    }
                )
                return assistant_message

            observation = self._execute_action(*action)

            self.conversation_history.append(
                {
                    "role": "user",
                    "content": f"Observation: {observation}",
                }
            )

    def _call_llm(self) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self.conversation_history,
        )
        return self._extract_text(response.content)

    @staticmethod
    def _extract_text(content) -> str:
        return " ".join(
            block.text
            for block in content
            if hasattr(block, "text")
        )

    @staticmethod
    def _parse_action(message: str):
        pattern = r"Action:\s*(\w+)(?::\s*(.*))?"
        match = re.search(pattern, message)

        if not match:
            return None

        tool_name = match.group(1)
        argument = match.group(2)

        return tool_name, argument

    @staticmethod
    def _execute_action(tool_name: str, argument: str | None):
        if tool_name not in TOOL_MAP:
            return f"Unknown tool '{tool_name}'."

        tool = TOOL_MAP[tool_name]

        if argument:
            return tool(argument)

        return tool()

    def clear_history(self):
        self.conversation_history.clear()

    def get_history(self):
        return self.conversation_history.copy()