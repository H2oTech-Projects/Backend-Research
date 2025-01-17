from celery import shared_task
import time

@shared_task
def process_data(data):
    print(f"Processing: {data}")
    time.sleep(5)  # Simulate a time-consuming task
    return f"Processed: {data}"

@shared_task
def send_email(to_email):
    print(f"Sending email to: {to_email}")
    time.sleep(2)
    return f"Email sent to: {to_email}"

