from celery import shared_task
import random
import requests
#import logging

#failed celery task

'''@shared_task
def task_process_notification():
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')
'''
#solution 1 : using Try/Except Block
# Define the logger
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
'''
@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 7, 'countdown': 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')
'''
#Exponential Backoff

'''@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')'''

#Randomness
'''@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_jitter=True, retry_kwargs={'max_retries': 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')'''

#Task Base Class

class BaseTaskWithRetry(celery.Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = True


@shared_task(bind=True, base=BaseTaskWithRetry)
def task_process_notification(self):
    raise Exception()
