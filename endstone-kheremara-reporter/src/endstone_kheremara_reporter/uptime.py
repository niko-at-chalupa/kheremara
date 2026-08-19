import time
from datetime import timedelta

class Uptime:
    def __init__(self):
        self._start = time.monotonic()
    
    @property
    def now(self) -> timedelta:
        elapsed_seconds = time.monotonic() - self._start
        return timedelta(seconds=elapsed_seconds)

def format_uptime(delta: timedelta) -> str:
    total_seconds = int(delta.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days > 0:
        day_str = "day" if days == 1 else "days"
        return f"up {days} {day_str}, {hours}:{minutes:02d}"
    elif hours > 0:
        return f"up {hours}:{minutes:02d}"
    else:
        return f"up {minutes} min"