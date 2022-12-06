from time import time
from functools import wraps
from rich import print


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        end = time()
        timed = (end - start) * 1000 * 1000
        print(
            f"[italic bright_cyan]{f.__name__}[/italic bright_cyan] [grey66]time:[/grey66] [bold magenta1]{timed:.2f} μs[/bold magenta1]"
        )
        return res

    return wrapper
