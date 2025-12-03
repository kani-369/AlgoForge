# utils/benchmark.py
# Simple benchmark runner for AlgoForge
import time
import importlib
import psutil
import traceback
from typing import Any, Dict

PROCESS = psutil.Process()

def _current_rss() -> int:
    return PROCESS.memory_info().rss

def measure_call(func, *args, **kwargs) -> Dict[str, Any]:
    """Measure time (ms) and memory (bytes) for a single call of func."""
    start_mem = _current_rss()
    start = time.perf_counter()
    try:
        output = func(*args, **kwargs)
        error = None
    except Exception as e:
        output = None
        error = {"type": type(e).__name__, "msg": str(e), "trace": traceback.format_exc()}
    end = time.perf_counter()
    end_mem = _current_rss()

    return {
        "time_ms": (end - start) * 1000.0,
        "mem_bytes_delta": max(0, end_mem - start_mem),
        "output": output,
        "error": error
    }

def _find_callable(mod, operation: str):
    """
    Heuristic to locate a callable inside module:
    - exact operation
    - operation with spaces -> underscores
    - run_<module>_operations
    - run_<operation> (underscored)
    """
    cand_names = []
    if operation:
        cand_names.append(operation)
        cand_names.append(operation.replace(" ", "_"))
        cand_names.append("run_" + operation.replace(" ", "_"))
    # module-level runner
    cand_names.append("run_" + getattr(mod, "__name__", "module").split(".")[-1] + "_operations")
    # generic fallback
    cand_names.append("run_operations")
    for name in cand_names:
        if hasattr(mod, name):
            obj = getattr(mod, name)
            if callable(obj):
                return obj
    return None

def run_benchmark(module_name: str, operation: str = None, *op_args, **op_kwargs) -> Dict[str, Any]:
    """
    Load modules.<module_name>, find a callable for the operation, and benchmark it.
    Returns a dict with timing, memory, and output/error.
    """
    try:
        mod = importlib.import_module(f"modules.{module_name}")
    except Exception as e:
        return {"error": {"type": type(e).__name__, "msg": f"Failed to import module '{module_name}': {e}"}}

    func = _find_callable(mod, operation or "")
    if func is None:
        return {"error": {"type": "NotFound", "msg": f"No callable found in module '{module_name}' for operation '{operation}'"}}

    # Call the function via measure_call
    result = measure_call(func, *op_args, **op_kwargs)
    # Add some metadata
    result["module"] = module_name
    result["operation"] = operation
    result["callable_name"] = func.__name__ if callable(func) else None
    return result

# quick manual test when run directly
if __name__ == "__main__":
    # Example: tries to run modules.divide_conquer.run_divide_conquer_operations()
    print(run_benchmark("divide_conquer", "run"))