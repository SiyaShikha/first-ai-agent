from dataclasses import dataclass
from typing import Callable

from tools.git_tools import (
    git_branch,
    git_diff,
    git_log,
    git_status,
)


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    function: Callable


TOOLS = [
    Tool(
        name="git_status",
        description="Returns the current status of the Git repository, including modified, staged, and untracked files.",
        function=git_status,
    ),
    Tool(
        name="git_log",
        description="Returns the five most recent commits in the repository.",
        function=git_log,
    ),
    Tool(
        name="git_branch",
        description="Returns the current branch and all available local branches.",
        function=git_branch,
    ),
    Tool(
        name="git_diff",
        description="Returns the current unstaged changes in the repository.",
        function=git_diff,
    ),
]


TOOL_MAP = {
    tool.name: tool.function
    for tool in TOOLS
}


def build_tool_prompt() -> str:
    """Build a formatted description of all available tools."""

    return "\n".join(
        f"- {tool.name}: {tool.description}"
        for tool in TOOLS
    )