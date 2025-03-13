"""Fixtures for the project directory."""

import shutil
import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

from tests_cookiecutter.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    """Yield a temporary project directory for tests."""
    test_session_id: str = generate_test_session_id()
    template_values = {"repo_name": f"test-repo-{test_session_id}"}
    generated_repo_dir: Path = generate_project(template_values=template_values, test_session_id=test_session_id)
    try:
        initialize_git_repo(repo_dir=generated_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
        yield generated_repo_dir
    finally:
        shutil.rmtree(path=generated_repo_dir, ignore_errors=True)


def generate_test_session_id() -> str:
    """Return a unique short test session ID."""
    test_session_id = str(uuid4())[:6]
    return test_session_id
