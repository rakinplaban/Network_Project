# Generated by Django 3.2.8 on 2022-01-11 18:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0027_newpost_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='likepost',
            field=models.ManyToManyField(blank=True, default=None, related_name='likepost', to=settings.AUTH_USER_MODEL),
        ),
    ]
