from . import celery_app
from raven.contrib.celery import register_logger_signal, register_signal
from raven.contrib.django.raven_compat.models import client

register_logger_signal(client)
register_logger_signal(client)
register_signal(client)
register_signal(client, ignore_expected=True)


@celery_app.task
def add(a, b):
    return a + b


add.delay(4, 5)
add.apply_async(args=(4, 5))
