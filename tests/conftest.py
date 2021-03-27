import pathlib

import pytest


@pytest.fixture()
def root_dir() -> pathlib.PosixPath:
    return pathlib.Path().absolute()
