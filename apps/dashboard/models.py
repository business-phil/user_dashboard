from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class Message(models.Model):
	message = models.CharField(max_length=1000)
	user = models.ForeignKey(User, related_name='usermessage')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
	comment = models.CharField(max_length=1000)
	user = models.ForeignKey(User, related_name='usercomment')
	message = models.ForeignKey(User, related_name='messagecomment')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
