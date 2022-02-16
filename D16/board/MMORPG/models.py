from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_name = models.OneToOneField(User, max_length=64, on_delete=models.CASCADE, related_name='author', blank=True)
    author_rating = models.IntegerField(default=0)
    author_icon = models.CharField(max_length=256, default='')
    # author_email = models.EmailField(default='', blank=True)
    # author_code = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.author_name}'

class Post(models.Model):
    post_author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_header = models.CharField(max_length=64)
    #post_text = models.TextField(max_length=256)
    post_rating = models.IntegerField(default=0)
    post_content = models.CharField(max_length=512, default='')
    CATEGORY_TYPES = (
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
    post_category = models.CharField(choices=CATEGORY_TYPES,max_length=10)

    def __str__(self):
        return f'{self.post_author.author_name} -- {self.post_header}'

    def like(self):
        self.post_rating += 1
        self.save()

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'http://127.0.0.1:8000/posts/{self.id}'

# class PostCategory(models.Model):
#     post_through = models.ForeignKey('Post',on_delete=models.CASCADE)
#     category_through = models.ForeignKey('Category',on_delete=models.CASCADE)


# class Category(models.Model):
#     TYPES = (
#         ("t","Танки"),
#         ("h","Хилы"),
#         ("DD","ДД"),
#         ("trad","Торговцы"),
#         ("gild","Гилдмастеры"),
#         ("qg","Квестгиверы"),
#         ("bs","Кузнецы"),
#         ("tan","Кожевники"),
#         ("pot","Зельевары"),
#         ("ms","Мастера заклинаний"),
#     )
#     category_type = models.CharField(choices=TYPES, max_length=10)


    # def __str__(self):
    #     return f'{self.category_type}'

class Comment(models.Model):
    comment_text = models.TextField(max_length=128)
    comment_date_time = models.DateTimeField(auto_now_add=True)
    comment_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_online = models.BooleanField(default=False)

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'http://127.0.0.1:8000/posts/myposts/replies/{self.comment_post.id}'

    # def get_approve(self):
    #     return 'http://127.0.0.1:8000/posts/myposts/replies/{self.comment_post.id}'


# class OneTimeCode(models.Model):
#     code = models.IntegerField(blank=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)



