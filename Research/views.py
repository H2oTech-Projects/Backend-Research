from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail.tasks import send_mail_task
def test(request):
    test_func.delay()

    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_task.delay()
    return HttpResponse("sent")
