

import time
import functools


def timer(func):
    """Decorator that prints how long a function takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def repeat(times):
    """Decorator factory that repeats a function call multiple times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@timer
def slow_function():
    time.sleep(1)
    print("Function finished")


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    slow_function()
    print("-" * 20)
    greet("World")