# Generated by Django 5.0 on 2023-12-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_jobseeker',
            field=models.BooleanField(default=False, verbose_name='Is jobseeker'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_recruiter',
            field=models.BooleanField(default=False, verbose_name='Is recruiter'),
        ),
    ]