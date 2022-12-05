import time
from functools import wraps
from rich import print


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        timed = (end - start) * 1000 * 1000
        print(
            f"[italic bright_cyan]{f.__name__}[/italic bright_cyan] [grey66]time:[/grey66] [bold magenta1]{int(timed)} μs[/bold magenta1]"
        )
        return res

    return wrapper
