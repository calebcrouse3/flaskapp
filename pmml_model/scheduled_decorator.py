
"""This class defines a decorator which can be used to make a function rerun at fixed intervals"""

import time
import functools


def scheduled(fixed_delay):
    def decorator_scheduled(func):
        functools.wraps(func)

        def wrapper_schedule(*args, **kwargs):
            result = func(*args, **kwargs)
            self = args[0]
            delay = getattr(self, fixed_delay)
            time.sleep(delay)
            return result
        return wrapper_schedule
    return decorator_scheduled