from celery import shared_task
from time import sleep

@shared_task
def test_task():
    sleep(10)
    return 'Helllllooooooo'
