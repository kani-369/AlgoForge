# algoforge/__init__.py
__version__ = "0.0.1"

# export registry helpers at package level for convenience
from .registry import register, get_algorithm, list_algorithms  # noqa: E402,F401
from .base import FunctionAlgorithm  # noqa: E402,F401