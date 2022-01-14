from django.contrib.auth.models import AbstractUser
from django.db import models

# def images(request):
    

class User(AbstractUser):
    pass

class NewPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    likepost = models.ManyToManyField(User, default=None, blank=True , related_name="likepost")

    def __str__(self):
        return f"{self.post}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(NewPost, on_delete= models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    picture = models.ImageField(blank=True,null=True,upload_to="images/")
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    followings = models.ManyToManyField(User,blank = True, related_name="followings")
    # post = models.ForeignKey(NewPost,null = True ,on_delete=models.CASCADE)

# class Following(models.Model):
#     user = models.