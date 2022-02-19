from django.db import models
from sign.models import User
from .models import Comment, Post
from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver
from .functions import send_code_by_mail,send_users_comment,send_users_like, send_approved_comment, send_notapproved_comment


@receiver(post_save, sender=Comment)
def send_comment_by_email(sender, instance, created, **kwargs):
    if created:
        comment = instance
        commented_user = instance.comment_user
        authors_post = instance.comment_post.post_author
        send_users_comment(authors_post,commented_user,comment)

@receiver(pre_save, sender=Comment)
def send_approved_comment_by_email(sender, instance, **kwargs):
    comment = instance
    commented_user = instance.comment_user
    author_post = instance.comment_post.post_author
    commented_post = instance.comment_post
    send_approved_comment(comment,commented_user,author_post,commented_post)

@receiver(post_delete, sender=Comment)
def send_notapproved_comment_by_email(sender, instance, **kwargs):
    comment = instance
    commented_post = instance.comment_post
    commented_user = instance.comment_user
    author_post = instance.comment_post.post_author
    send_notapproved_comment(comment,commented_user,author_post,commented_post)


# @receiver(pre_save, sender=Post)
# def send_like_by_email(sender, instance, **kwargs):
#     liked_post = instance
#     author_post = instance.post_author
#     author_user = User.objects.get(username=author_post.author_name)
#     author_email = author_user.email
#     send_users_like(author_post,liked_post, author_email)









