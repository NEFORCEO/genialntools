import time
import threading
from functools import wraps


class Slowed:
    def __call__(self, delay: float = 1.0):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                time.sleep(delay)
                return func(*args, **kwargs)
            return wrapper
        return decorator


class Speed:
    def __call__(self, repeat: int = 1):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                def run():
                    for _ in range(repeat):
                        func(*args, **kwargs)

                t = threading.Thread(target=run)
                t.start()
                return t 
            return wrapper
        return decorator
