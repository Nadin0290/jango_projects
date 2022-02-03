import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from django.db.models.signals import post_save
from django.dispatch import receiver
from ...models import Subscriber, Post
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


logger = logging.getLogger(__name__)


# наша задача по выводу текста на экран
def my_job():
    #  Your job processing logic here...
    # instance = Post.objects.filter(date__range=["2011-01-01", "2011-01-31"])
    instance = Post.objects.all().order_by('-id')[:5] # не знаю как отфильтровать по последней дате (что бы она не была статическая) напишите пожалуйста как
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        html_content = render_to_string(
            'news_app/mail_every_week.html',
            {
                'post': instance,
                'subscriber': subscriber
            }
        )
        msg = EmailMultiAlternatives(
            subject= f'Новые посты за эту неделю!',
            from_email= 'arseniy.reima@gmail.com',
            to=[subscriber.email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем



# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=1200_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/604800"),  # в одной неделе 604800 секунд :D
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")