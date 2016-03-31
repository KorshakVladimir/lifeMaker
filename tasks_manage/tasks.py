from celery import shared_task

@shared_task
def get_mes():
    print('my message')