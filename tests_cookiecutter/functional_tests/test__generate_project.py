"""Tests for template."""

from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """Check that the generated project directory exists."""
    assert project_dir.exists()
