# algoforge/registry.py
from typing import Dict, List
from .base import Algorithm

# internal registry mapping name -> Algorithm
_REGISTRY: Dict[str, Algorithm] = {}

def register(algo: Algorithm) -> None:
    """
    Register an Algorithm instance.
    Raises ValueError if name already exists.
    """
    name = getattr(algo, "name", None)
    if not name:
        raise ValueError("Algorithm must have a 'name' attribute")
    if name in _REGISTRY:
        raise ValueError(f"Algorithm already registered: {name}")
    _REGISTRY[name] = algo

def unregister(name: str) -> None:
    """Remove algorithm from registry if present."""
    _REGISTRY.pop(name, None)

def get_algorithm(name: str) -> Algorithm:
    """Retrieve Algorithm by exact name. Raises KeyError if not found."""
    return _REGISTRY[name]

def list_algorithms(prefix: str = None) -> List[str]:
    """List registered algorithm names. If prefix supplied, filter by prefix."""
    keys = list(_REGISTRY.keys())
    if prefix:
        keys = [k for k in keys if k.startswith(prefix)]
    return sorted(keys)

def clear_registry() -> None:
    """Remove all registered algorithms (useful for tests)."""
    _REGISTRY.clear()