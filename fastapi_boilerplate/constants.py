from enum import Enum


class RunServer(str, Enum):
    CLI = "CLI"
    PYTHON = "Python"


class YesOrNo(str, Enum):
    YES = "y"
    NO = "n"


class Packaging(str, Enum):
    POETRY = "poetry"
    PIP = "pip"
    POETRY_WITH_REQUIREMENTS = "poetry with requirements"
