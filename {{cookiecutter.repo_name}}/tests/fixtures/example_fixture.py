"""Defines fixtures that can be used in the tests."""

from uuid import uuid4

import pytest

from tests.consts import PROJECT_DIR


@pytest.fixture(scope="session")
def generate_test_session_id() -> str:
    """
    Generate a unique test session identifier.

    This fixture creates a test session identifier by concatenating the project directory's name
    with the first six characters of a newly generated UUID. The resulting string serves as a unique
    identifier for the entire test session.

    Returns
    -------
    str
        A unique test session identifier.

    """
    test_session_id = str(PROJECT_DIR.name) + str(uuid4())[:6]
    return test_session_id
