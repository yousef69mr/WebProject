# Generated by Django 3.2.5 on 2022-04-25 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_login_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student', verbose_name='Student'),
        ),
    ]