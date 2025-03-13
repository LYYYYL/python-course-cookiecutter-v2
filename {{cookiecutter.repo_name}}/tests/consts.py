"""
Stores constants used in the tests.

Defines PROJECT_DIR to be used in the tests.
"""

from pathlib import Path

THIS_DIR = Path(__file__).parent
PROJECT_DIR = (THIS_DIR / "../").resolve()
