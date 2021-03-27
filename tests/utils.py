import os
import subprocess
from pathlib import Path, PosixPath
from typing import List


def run_cookiecutter(root_dir: Path, tmp_path: Path, config_path: Path) -> None:
    subprocess.run(
        [
            "cookiecutter",
            root_dir,
            "--output-dir",
            tmp_path,
            "--config-file",
            config_path,
            "--no-input",
        ]
    )


def _build_tree(structure: str):
    files = []
    previous_level = -1
    stack = ["/"]
    for line in structure.splitlines()[1:]:
        name = line.strip()
        level = line.count(" ") // 4
        if previous_level > level:
            stack.pop()
        files.append(Path(*stack, name))
        if name.endswith("/"):
            stack.append(name)
        previous_level = level
    return files


def list_structures(tmp_path: Path, structure: str):
    tree = _build_tree(structure)
    current: List[PosixPath] = []
    base_path = str(tmp_path)
    for root, files, dirs in os.walk(tmp_path):
        base_dir = root[root.startswith(base_path) and len(base_path) :]
        current.extend(Path("/", base_dir) / file for file in files)
        current.extend(Path("/", base_dir) / dir for dir in dirs)
    return set(str(path) for path in current), set(str(path) for path in tree)
