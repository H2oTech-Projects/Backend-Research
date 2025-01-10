from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')

app = Celery('Backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    broker_url='redis://localhost:6379/0',
    CELERY_WORKER_POOL='solo'
)

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
