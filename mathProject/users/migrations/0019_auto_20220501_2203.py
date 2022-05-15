# Generated by Django 3.2.5 on 2022-05-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20220501_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Email Verified'),
        ),
    ]