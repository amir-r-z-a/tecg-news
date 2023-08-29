import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
import subprocess

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_news.settings")
app = Celery("tech_news")
# celery = Celery('task', broker='redis://127.0.0.1:6379')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(30.0, test.s(), name='scrapper every 30')

# # Calls test('hello') every 30 seconds.
# # It uses the same signature of previous task, an explicit name is
# # defined to avoid this task replacing the previous one defined.
# sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')
#
# # Calls test('world') every 30 seconds
# sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
# # Executes every Monday morning at 7:30 a.m.
# sender.add_periodic_task(
#     crontab(hour=7, minute=30, day_of_week=1),
#     test.s('Happy Mondays!'),
# )


@app.task(bind=True)
def test(arg):
    print(arg)
    script_path = "/home/amirreza/Desktop/roshan2/tech-news/tech_news/scrapper.py"
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


# app.conf.beat_schedule = {
#     'scrap every 30': {
#         'task': 'tasks.test',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'
