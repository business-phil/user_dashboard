from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    pass

class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    user_level = models.CharField(
        max_length=5,
        choices=(('user', 'User'), ('admin', 'Admin')),
        default='user')
    description = models.TextField(max_length=400, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()
