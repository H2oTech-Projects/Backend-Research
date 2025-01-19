from celery import shared_task
from celery import Task
import random
import requests
import logging

#failed celery task
#The task_process_notification task raises a random exception (50% chance) or makes a POST request to https://httpbin.org/delay/5, which delays the response for 5 seconds.
'''@shared_task
def task_process_notification():
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')
'''
#solution 1 : using Try/Except Block
# Define the logger
#The task_process_notification task randomly raises an exception or makes a POST request, logs errors, and retries the task after 5 seconds if an exception occurs.
'''logger = logging.getLogger(__name__)

@shared_task(bind=True)
def task_process_notification(self):
    try:
        # Randomly raise an exception to simulate a failure
        if not random.choice([0, 1]):
            raise Exception("Simulated random failure")

        # Make a POST request
        requests.post('https://httpbin.org/delay/5')
    except Exception as e:
        # Log the exception
        logger.error('Exception raised, task will retry after 5 seconds: %s', str(e))
        
        # Retry the task
        raise self.retry(exc=e, countdown=5)
'''

#Solution 2: Task Retry Decorator
#The task_process_notification task randomly raises an exception or makes a POST request, and will automatically retry up to 7 times with a 5-second delay if an exception occurs.
'''@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 7, 'countdown': 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')'''

#Exponential Backoff
#The task_process_notification task randomly raises an exception or makes a POST request, and if an exception occurs, it will automatically retry up to 5 times with increasing delays between retries (retry_backoff=True).
'''
@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')
'''
#Randomness
#The task retries up to 5 times with backoff and random jitter if an exception occurs.
'''@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_jitter=True, retry_kwargs={'max_retries': 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')
'''
#Task Base Class
#The task task_process_notification inherits retry behavior from BaseTaskWithRetry, automatically retrying up to 5 times with backoff if an exception occurs.
class BaseTaskWithRetry(Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = True


@shared_task(bind=True, base=BaseTaskWithRetry)
def task_process_notification(self):
    raise Exception()
