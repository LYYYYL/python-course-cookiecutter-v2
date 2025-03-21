"""Utility functions for generating a project using cookiecutter."""

import json  # noqa: I001
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

from tests_cookiecutter.constants import PROJECT_DIR


def initialize_git_repo(repo_dir: Path):
    """Initialize a git repository in the given directory."""
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "'feat: initial commit by pytest'"], cwd=repo_dir, check=True)


def generate_project(template_values: Dict[str, str], test_session_id: str) -> Path:
    """Generate a project with cookiecutter and return its directory."""
    template_values_copy: Dict[str, str] = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values_copy}
    cookiecutter_config_fpath = PROJECT_DIR / f"cookiecutter-{test_session_id}-test-config.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)

    generated_repo_dir: Path = PROJECT_DIR / "sample" / template_values["repo_name"]
    return generated_repo_dir
