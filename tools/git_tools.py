import subprocess

def _run_git_command(args: list[str]) -> str:
    """Run a Git command and return its output."""

    try:
        result = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()

    except subprocess.CalledProcessError as error:
        return error.stderr.strip()


def git_status() -> str:
    return _run_git_command(["status"])


def git_log() -> str:
    return _run_git_command([
        "log",
        "--oneline",
        "-5",
    ])


def git_branch() -> str:
    return _run_git_command(["branch"])


def git_diff() -> str:
    return _run_git_command(["diff"])