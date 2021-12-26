from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from django.http import request
from .models import Subscriber, Post, Category
from django.core.mail import mail_admins
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string
from .tasks import send_subscribers


# уведомляем подписчиков (всех) о новой статье, мой комментарий по этому поводу  чуть ниже
@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    send_subscribers(instance.id)

#     if created: # если пост создан
#         if instance.author.is_blocked == False: # если автор не привысил кол-во созданий постов
#             for subscriber in Subscriber.objects.all(): #информируем всех о новом посте

#                 html_content = render_to_string(
#                     'news_app/mail_subscribers.html',
#                     {
#                         'post': instance,
#                         'subscriber': subscriber,
#                         'category' : subscriber.category
#                     }
#                 )
#                 msg = EmailMultiAlternatives(
#                     subject= f'Создали новость новую статью!',
#                     from_email= 'arseniy.reima@gmail.com',
#                     to=[subscriber.email],  # разсылаем каждому подписчику на почту
#                 )
#                 msg.attach_alternative(html_content, "text/html")  # добавляем html

#                 msg.send()  # отсылаем



#             # print(subscriber.email)
#         else: # автор получает личное письмо о том что он забанен
#             html_content = render_to_string(
#                 'news_app/report_author.html',
#                 {
#                     'post': instance,
#                 }
#             )
#             msg = EmailMultiAlternatives(
#                 subject= f'Вы превысили кол-во созданий!',
#                 from_email= 'arseniy.reima@gmail.com',
#                 to=[instance.author.author_name.email],
#             )
#             msg.attach_alternative(html_content, "text/html")  # добавляем html

#             msg.send()  # отсылаем



# # уведомляем подписчика, что он подписался
# @receiver(post_save, sender=Subscriber)
# def notify_new_subscriber(sender, instance, created, **kwargs):

#     if created: # если добавился подписчик

#         html_content = render_to_string(
#             'news_app/mail_new_subscribers.html',
#             {
#                 'subscriber': instance,
#             }
#         )

#         msg = EmailMultiAlternatives(
#             subject= f'Вы подписались на категорию {instance.category.category_name}',
#             from_email= 'arseniy.reima@gmail.com',
#             to=[instance.email],  # это то же, что и recipients_list
#         )
#         msg.attach_alternative(html_content, "text/html")  # добавляем html

#         msg.send()  # отсылаем
