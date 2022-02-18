from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, default='')
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, default='')
    avatar = models.ImageField(default='images/avatar.svg')

    REQUIRED_FIELDS = 'email'
    REQUIRED_FIELDS = []