import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = { # не могу проверить работоспособность тк работаю на винде.. трудности начинаются даже при обычном использовании Celery
    'action_every_monday_8am': {
        'task': 'NewsApp.tasks.send_email_weekly',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}