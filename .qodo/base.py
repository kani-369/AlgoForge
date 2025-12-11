# algoforge/base.py
from typing import Callable, Any, Dict, Protocol, runtime_checkable

@runtime_checkable
class Algorithm(Protocol):
    """
    Minimal interface for an algorithm plugin.
    Implementations must provide:
      - name: unique string
      - run(*args, **kwargs) -> Any
      - metadata: optional dict with keys like category
    """
    name: str
    def run(self, *args, **kwargs) -> Any: ...
    metadata: Dict[str, Any]

class FunctionAlgorithm:
    """
    Lightweight wrapper to turn a plain function into an Algorithm.
    Usage:
      def my_algo(data): ...
      alg = FunctionAlgorithm("my_algo", my_algo, metadata={"category":"sort"})
      register(alg)  # registry.register imported elsewhere
    """
    def __init__(self, name: str, func: Callable, metadata: Dict[str,Any]=None):
        self.name = name
        self.func = func
        self.metadata = metadata or {}

    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<FunctionAlgorithm name={self.name} meta={self.metadata}>"