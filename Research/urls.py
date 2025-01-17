from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.test , name='test'),
    path('sendmail/', views.send_mail_to_all , name='send_mail'),
    path('schedulemail/', views.schedule_mail , name='schedule-mail'),
    path('task-process/', views.trigger_task , name='task_process'),

]
