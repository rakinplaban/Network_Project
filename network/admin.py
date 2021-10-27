from django.contrib import admin
from .models import User, NewPost
# Register your models here.

class User_display(admin.ModelAdmin):
    list_display = ("id","username","password")

class Post_display(admin.ModelAdmin):
    list_display = ("id","post","user","timestamp")

admin.site.register(User,User_display)
admin.site.register(NewPost,Post_display)