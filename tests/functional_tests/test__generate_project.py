import json  # noqa: I001
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import (
    Dict,
    Generator,
)

import pytest



def test__can_generate_project(project_dir: Path):
    assert project_dir.exists()
