import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from todo.models import Todo
from django.utils import timezone
from datetime import timedelta
import pytz
from django.core.mail import send_mass_mail
from celery.schedules import crontab

from celery import shared_task, task
from celery.decorators import periodic_task


"""@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(
            get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user( 
            username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)"""


@periodic_task(
    run_every=(crontab(minute="*/03")),
    name=" scheduling deadline", ignore_result=True
)
def send_notification():

    start = timezone.now()

    end = start + timedelta(minutes=60)
    getInfo = Todo.objects.filter(deadline__range=[start, end])

    if getInfo:

        for i in getInfo:

            message = ('Pockito alert', '{} at {}'.format(
                i.description, i.deadline), 'webmaster@localhost', [i.author.email])
            send_mass_mail((message,), fail_silently=False)
        return "Success"

    else:
        return "No enent"
