from celery import shared_task
from .models import Post, Subscriber

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import time

# Реализовать рассылку уведомлений подписчикам после создания новости.
@shared_task
def send_subscribers(pid):
    post = Post.objects.get(pk=pid) # находим наш пост

    for subscriber in Subscriber.objects.all():
        html_content = render_to_string(
            'news_app/mail_subscribers.html',
            {
                'post': post,
                'subscriber': subscriber,
                'category' : subscriber.category
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Создали новость новую статью!',
            from_email= 'arseniy.reima@gmail.com',
            to=[subscriber.email],  # разсылаем каждому подписчику на почту
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем


# Реализовать еженедельную рассылку с последними новостями (каждый понедельник в 8:00 утра).
@shared_task
def send_email_weekly():
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


# @shared_task
# def hello():
#     print("HGello world!")
