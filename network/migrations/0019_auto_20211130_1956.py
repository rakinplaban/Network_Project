# Generated by Django 3.1.3 on 2021-11-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_auto_20211130_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
