from django.db import models
from sign.models import User


class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_header = models.CharField(max_length=64)
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
        return f'{self.post_author.username} -- {self.post_header}'

    def like(self):
        self.post_rating += 1
        self.save()

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'http://127.0.0.1:8000/posts/{self.id}'


class Comment(models.Model):
    comment_text = models.TextField(max_length=128)
    comment_date_time = models.DateTimeField(auto_now_add=True)
    comment_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_online = models.BooleanField(default=False)

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'http://127.0.0.1:8000/posts/myposts/replies/{self.comment_post.id}'



