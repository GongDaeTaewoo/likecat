# Generated by Django 4.2 on 2023-04-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_myuser_age_alter_myuser_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
