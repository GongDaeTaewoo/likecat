# Generated by Django 4.2 on 2023-04-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_myuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('남성', '님성'), ('여성', '여성')], max_length=7),
        ),
    ]
