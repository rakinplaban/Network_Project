from django.contrib import admin
from .models import User
# Register your models here.

class User_display(admin.ModelAdmin):
    list_display = ("id","username","password")

admin.site.register(User,)
