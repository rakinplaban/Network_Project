from django.contrib import admin
from .models import User, NewPost, Profile
# Register your models here.

class User_display(admin.ModelAdmin):
    list_display = ("id","username","password")

class Post_display(admin.ModelAdmin):
    list_display = ("id","post","user","timestamp")

class Profile_display(admin.ModelAdmin):
    list_display = ("id" , "user" , "picture" , "following", "follower")

admin.site.register(User,User_display)
admin.site.register(NewPost,Post_display)
admin.site.register(Profile,Profile_display)