# Generated by Django 3.2.5 on 2022-05-14 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('users', '0028_auto_20220507_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'ordering': ['id'], 'verbose_name': 'Admin'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id'], 'verbose_name': 'Student'},
        ),
        migrations.AlterField(
            model_name='login',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.level', verbose_name='Education level'),
        ),
        migrations.AlterField(
            model_name='login',
            name='loginMethod',
            field=models.CharField(choices=[('email', 'By Email'), ('code', 'By Code'), ('username', 'By Username')], max_length=10, null=True),
        ),
    ]
