"""
Feature: Function Logger Decorator
Description:
Logs function name, arguments, and execution time.
Can log to console and optionally to a file.
"""

import time
from functools import wraps

def log_function(log_to_file: bool = False, filename: str = "logs.txt"):
    """
    Decorator to log function execution details.

    Args:
        log_to_file (bool): If True, also write logs to a file.
        filename (str): File to write logs if log_to_file is True.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            exec_time = end_time - start_time

            arg_list = [repr(a) for a in args] + [f"{k}={v!r}" for k,v in kwargs.items()]
            arg_str = ", ".join(arg_list)
            log_msg = f"[LOG] Function '{func.__name__}' called with ({arg_str}) -> Execution time: {exec_time:.6f}s"

            # Log to console
            print(log_msg)

            # Optionally log to file
            if log_to_file:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_msg + "\n")

            return result
        return wrapper
    return decorator
