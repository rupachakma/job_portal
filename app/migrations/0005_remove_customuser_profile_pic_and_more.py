# Generated by Django 5.0 on 2023-12-12 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customuser',
            name='display_name',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]
