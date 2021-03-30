"""Test cookiecutter generation.

Reference:
- https://stackoverflow.com/questions/4187564/recursively-compare-two-directories-to-ensure-they-have-the-same-files-and-subdi
"""

import filecmp
import os
import subprocess
from pathlib import Path

import pytest
import yaml


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


class dircmp(filecmp.dircmp):
    """
    Compare the content of dir1 and dir2. In contrast with filecmp.dircmp, this
    subclass compares the content of files with the same path.
    """

    def phase3(self):
        """
        Find out differences between common files.
        Ensure we are using content comparison with shallow=False.
        """
        fcomp = filecmp.cmpfiles(
            self.left, self.right, self.common_files, shallow=False
        )
        self.same_files, self.diff_files, self.funny_files = fcomp


def is_same(dir1, dir2):
    """
    Compare two directory trees content.
    Return False if they differ, True is they are the same.
    """
    compared = dircmp(dir1, dir2)
    if (
        compared.left_only
        or compared.right_only
        or compared.diff_files
        or compared.funny_files
    ):
        assert False, (dir1, dir2, compared.diff_files)
    for subdir in compared.common_dirs:
        subdir1 = os.path.join(dir1, subdir)
        subdir2 = os.path.join(dir2, subdir)
        if not is_same(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            assert False, (os.listdir(subdir1), os.listdir(subdir2))
    return True


@pytest.mark.parametrize("config_path", ["simple", "docker"])
def test_cookiecutter(tmp_path: Path, root_dir: Path, config_path: str):
    project_path = root_dir / f"tests/resources/{config_path}"
    config_file = project_path / "config.yaml"
    run_cookiecutter(root_dir, tmp_path, config_file)
    with open(config_file, "r") as stream:
        project_slug = yaml.safe_load(stream)["default_context"]["project_slug"]
    is_same(tmp_path / project_slug, project_path / project_slug)
