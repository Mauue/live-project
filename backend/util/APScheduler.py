from apscheduler.schedulers.blocking import BlockingScheduler

from main import scheduler
from db import get_db
from util.draw import draw_mask


def new_task():
    _, cursor = get_db()
    cursor.execute("SELECT end_time FROM order_set WHERE status=0")
    rounds = cursor.fetchall()
    if rounds is None:
        return
    for round in rounds:
        scheduler.add_job(func=draw_mask, next_run_time=round['end_time'])

