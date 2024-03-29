# Generated by Django 3.2.5 on 2022-05-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='loginMethod',
            field=models.CharField(choices=[('email', 'By Email'), ('code', 'By Code'), ('username', 'By Username')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(help_text='Required. 200 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=200, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, help_text='Designates whether the user verified his account or not.', verbose_name='Email Verified'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True),
        ),
    ]
