from django.contrib.auth.models import AbstractUser
from django.db import models

# def images(request):
    

class User(AbstractUser):
    pass

class NewPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.post}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    picture = models.ImageField(null=True,blank=True,upload_to="images/")
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default = 0)
    # post = models.ForeignKey(NewPost,null = True ,on_delete=models.CASCADE)


        
    