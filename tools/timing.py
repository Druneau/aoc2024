import time
from functools import wraps


def time_execution(func):
    """A decorator to time a function's execution in milliseconds."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_time_ms = (end - start) * 1000
        print(f"Function '{func.__name__}' executed in {execution_time_ms:.3f} ms")
        return result

    return wrapper
