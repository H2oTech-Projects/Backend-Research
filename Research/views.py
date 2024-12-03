from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail.tasks import send_mail_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

def test(request):
    test_func.delay()

    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_task.delay()
    return HttpResponse("sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=13, minute=52)
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name="schedule_mail_task_"+"10",
        task='send_mail.tasks.send_mail_task',
       # args=json.dumps([2, 3])
    )
    return HttpResponse("done")