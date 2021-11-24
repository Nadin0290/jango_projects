from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

class Author(models.Model):

    author_name = models.OneToOneField(User, max_length=64, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author_name}'


    def update_rating(self):
        postRating = self.post_set.all().aggregate(rating =Sum('rating'))
        pRating = 0
        pRating += postRating.get('rating')


        commentRating = self.author_name.comment_set.all().aggregate(rating = Sum('rating'))
        cRating = 0
        cRating += commentRating.get('rating')

        self.author_rating = pRating * 3 + cRating
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.category_name}'

class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    News = "NW"
    Article = 'AR'
    TYPES = (
        (News, 'Новость'),
        (Article, 'Статья')
    )
    category_type = models.CharField(choices=TYPES, max_length=2, default=Article)
    date_time = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=64)
    text = models.CharField(max_length=128)
    rating = models.IntegerField(default=0)
    post_category = models.ManyToManyField(Category, through="PostCategory")

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:120] + '...' + self.rating

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
            return f'/news/{self.id}'

class PostCategory(models.Model):
    post_through = models.ForeignKey(Post,on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category,on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=64)
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()





