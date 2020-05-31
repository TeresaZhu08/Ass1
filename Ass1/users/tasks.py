from __future__ import absolute_import, unicode_literals

from celery import shared_task
from users.models import Profile


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Profile.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Profile.objects.get(id=widget_id)
    w.name = name
    w.save()

