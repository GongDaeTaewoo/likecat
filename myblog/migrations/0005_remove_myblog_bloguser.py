# Generated by Django 4.2 on 2023-05-01 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_alter_myblog_bloguser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myblog',
            name='Bloguser',
        ),
    ]
