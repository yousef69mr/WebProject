# Generated by Django 3.2.5 on 2022-05-27 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20220514_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
