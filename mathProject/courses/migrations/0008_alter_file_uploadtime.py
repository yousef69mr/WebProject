# Generated by Django 3.2.5 on 2022-06-01 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_rating_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploadTime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Upload Time'),
        ),
    ]