# Generated by Django 3.2.5 on 2022-05-14 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20220514_1747'),
        ('courses', '0003_alter_lecture_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.subject', verbose_name='Educational Subject'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.subject', verbose_name='Educational Subject'),
        ),
    ]
