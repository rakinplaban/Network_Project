# Generated by Django 3.2.8 on 2022-01-08 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_auto_20220105_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
