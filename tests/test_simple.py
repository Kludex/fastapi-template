from pathlib import Path

from tests.utils import match_structure, run_cookiecutter

DIR_STRUCTURE = """
simple-project/
    app/
        api/
            v1/
                __init__.py
                home.py
            __init__.py
        __init__.py
        main.py
    tests/
        __init__.py
        conftest.py
    README.md
    setup.cfg
"""


def test_structure(tmp_path: Path, root_dir: Path):
    config_file = root_dir / "examples/simple/config.yaml"
    run_cookiecutter(root_dir, tmp_path, config_file)
    assert match_structure(tmp_path, DIR_STRUCTURE)
