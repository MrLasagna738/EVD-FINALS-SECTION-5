"""Daily Brew - open / closed status (Member 4).

Events used here:
  timer -> the status line refreshes every minute
"""
from datetime import datetime, timedelta, timezone

from js import setInterval
from pyodide.ffi import create_proxy
from pyscript import document


def update_status():
    # Philippine time is UTC+8
    now = datetime.now(timezone.utc) + timedelta(hours=8)
    el = document.querySelector("#open-status")
    if 10 <= now.hour < 22:
        mins_left = (22 - now.hour) * 60 - now.minute
        h, m = divmod(mins_left, 60)
        el.textContent = f"We're open now. Closing in {h}h {m}m."
        el.classList.add("open")
    else:
        el.classList.remove("open")
        el.textContent = "We're closed right now. Open daily, 10 AM to 10 PM."


def init():
    update_status()
    setInterval(create_proxy(update_status), 60000)
