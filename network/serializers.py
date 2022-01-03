from django.contrib.auth import models
from rest_framework import serializers
from .models import NewPost

class EditPostSerializer(serializers.ModelSerializer):
    class meta:
        model = NewPost
        fields = ('id','user','post','timestamp')
