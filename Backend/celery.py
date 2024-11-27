
from __future__ import absolute_import, unicode_literals
from celery import Celery

import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Backend.settings')


app = Celery('Backend')
app.conf.enable_utc = False
app.conf.update(timezone ='Asia/Kathmandu')

app.config_from_object(settings, namespace='CELERY')

#CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'request: {self.request}')
