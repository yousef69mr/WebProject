# Generated by Django 3.2.5 on 2022-05-31 10:31

import courses.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20220514_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='media/defaults/avatar.svg', null=True, upload_to='media/profile_images/%y/%m/%d', validators=[courses.validators.validate_image_file_extension]),
        ),
    ]
