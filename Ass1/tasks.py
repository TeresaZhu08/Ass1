from . import celery_app
from datetime import timedelta
from raven.contrib.celery import register_logger_signal, register_signal
from raven.contrib.django.raven_compat.models import client

register_logger_signal(client)
register_logger_signal(client)
register_signal(client)
register_signal(client, ignore_expected=True)

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}

CELERY_TIMEZONE = 'UTC'


@celery_app.task
def add(a, b):
    return a + b


add.delay(4, 5)
add.apply_async(args=(4, 5))
