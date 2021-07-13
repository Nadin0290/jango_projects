from django.db import models
from django.contrib.auth.models import User

# Author -- User
#------------------------------------------------------------

class Author(models.Model):
    author_name = models.OneToOneField(User,on_delete=models.CASCADE)
    rating_of_Author = models.IntegerField(default=0)


    def update_rating(self):
        postRat = self.post_set.aggregate(post_rating = models.Sum('rating_of_post'))
        pRat = 0
        pRat += postRat.get('post_rating') 

        comRat = self.author_name.comment_set.aggregate(comment_rating = models.Sum('rating_of_comment'))
        cRat = 0
        cRat += comRat.get('comment_rating') 

        self.rating_of_Author = pRat * 3 + cRat
        self.save()
 
#------------------------------------------------------------

# Category -- Post -- PostCategory -- Comment

#------------------------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=10,unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    what_post = models.CharField(default='news',max_length=255)
    date_and_time = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField('Category',through='PostCategory')
    heading = models.CharField(max_length=32,default='Heading')
    text = models.TextField(max_length=1024,default='Your text...')
    rating_of_post = models.IntegerField(default=0)
    
    def like(self):
        if self.rating_of_post > 0:
            self.rating_of_post += 1
        self.save()

            
    def dislike(self):
        if self.rating_of_post > 0:
            self.rating_of_post -= 1
        self.save()


    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.heading.title()}: {self.text[:20]}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User,on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=512,default='My comment')
    date_and_time = models.DateTimeField(auto_now_add=True)
    rating_of_comment = models.PositiveIntegerField(default=0)

    def like(self):
        self.rating_of_comment += 1
        self.save()
            
    def dislike(self):
        self.rating_of_comment -= 1
        self.save()


    def __str__(self):
        return f'{self.user_comment.username} -> {self.text_comment} \n Rating:{self.post.author.rating_of_Author} \n\n'
#------------------------------------------------------------
