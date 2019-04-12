from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
from django.core.management import call_command

from task_scheduler import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_scheduler.settings')
celery = Celery('tasks', broker='amqp://guest@localhost//')
app = Celery('task_scheduler')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'rate': {
        'task': 'open_exchange_rates',
        'schedule': timedelta(seconds=6),
    },
}

from celery.task import task
from urllib2 import Request, urlopen
import requests


@task(name="open_exchange_rates")
def rate():
    print "unit_updateunit_updateunit_updateunit_update"
    return "request.get('timestamp')"