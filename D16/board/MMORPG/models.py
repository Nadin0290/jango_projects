from random import Random
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=64, blank=True)

class Post(models.Model):
    header = models.CharField(max_length=64)
    text = models.TextField(max_length=256)
    rating = models.IntegerField(default=0)
    content = models.CharField(max_length=128, default='')
    post_category = models.ManyToManyField('Category', through='PostCategory')

    def __str__(self):
        return f'{self.header} {self.text[:10]}'

    def like(self):
        self.rating += 1
        self.save()


class PostCategory(models.Model):
    post_through = models.ForeignKey('Post',on_delete=models.CASCADE)
    category_through = models.ForeignKey('Category',on_delete=models.CASCADE)


class Category(models.Model):
    TYPES = (
        ("t","Танки"),
        ("h","Хилы"),
        ("DD","ДД"),
        ("trad","Торговцы"),
        ("gild","Гилдмастеры"),
        ("qg","Квестгиверы"),
        ("bs","Кузнецы"),
        ("tan","Кожевники"),
        ("pot","Зельевары"),
        ("ms","Мастера заклинаний"),
    )
    category_type = models.CharField(choices=TYPES, max_length=10)

class Comment(models.Model):
    text = models.TextField(max_length=128)
    date_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

# class OneTimeCode(models.Model):
#     code = models.IntegerField(default='1111')
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)



