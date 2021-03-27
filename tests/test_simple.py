from pathlib import Path

from tests.utils import list_structures, run_cookiecutter

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
        test_home.py
    README.md
    setup.cfg
    pyproject.toml
"""


def test_structure(tmp_path: Path, root_dir: Path):
    config_file = root_dir / "examples/simple/config.yaml"
    run_cookiecutter(root_dir, tmp_path, config_file)
    current, expected = list_structures(tmp_path, DIR_STRUCTURE)
    assert current == expected
