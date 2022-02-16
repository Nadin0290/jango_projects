from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# def send_congr_by_mail(username,email):
#         html_content = render_to_string(
#             'MMORPG/cong_mail.html',
#             {
#                 'username': username,
#             }
#         )

#         msg = EmailMultiAlternatives(
#             subject= f'Подтвердите вашу почту, {username}!',
#             from_email= 'arseniy.reima@gmail.com',
#             to=[email],  # это то же, что и recipients_list
#         )
#         msg.attach_alternative(html_content, "text/html")  # добавляем html

#         msg.send()  # отсылаем




def send_code_by_mail(email,code):
        html_content = render_to_string(
            'sign/send_code_mail.html',
            {
                'code':code,
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Подтвердите вашу почту!',
            from_email= 'arseniy.reima@gmail.com',
            to=[email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

def send_users_comment(author,user,comment):
        html_content = render_to_string(
            'MMORPG/mail/send_comment.html',
            {
                'author': author,
                'user':user,
                'comment':comment,
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Вам оставили отзыв!',
            from_email= 'arseniy.reima@gmail.com',
            to=[author.email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

def send_users_like(author,post,email):
        html_content = render_to_string(
            'MMORPG/mail/send_like.html',
            {
                'post': post,
                'author':author,
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Вам поставили лайк!',
            from_email= 'arseniy.reima@gmail.com',
            to=[email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

def send_approved_comment(comment,user,author,post):
        html_content = render_to_string(
            'MMORPG/mail/send_approved_comment.html',
            {
                'user':user,
                'comment':comment,
                'author':author,
                'post':post,
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Ваш комментарий принял автор!',
            from_email= 'arseniy.reima@gmail.com',
            to=[user.email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

def send_notapproved_comment(comment,user,author,post):
        html_content = render_to_string(
            'MMORPG/mail/send_notapproved_comment.html',
            {
                'comment':comment,
                'user':user,
                'author':author,
                'post':post,
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Ваш комментарий удалил автор!',
            from_email= 'arseniy.reima@gmail.com',
            to=[user.email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

def mailing(user,email,posts):
        html_content = render_to_string(
            'MMORPG/mail/mailing.html',
            {
                'user':user,
                'posts':posts,
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Новые посты, не пропустите важные обьявления!',
            from_email= 'arseniy.reima@gmail.com',
            to=[email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем