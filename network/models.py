from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class NewPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"post : {post} || user: {user} || timestamp: {timestamp} "