# Generated by Django 3.1.3 on 2021-11-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20211130_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
