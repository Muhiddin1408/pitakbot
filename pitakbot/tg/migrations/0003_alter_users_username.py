# Generated by Django 4.0.2 on 2022-02-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0002_rename_user_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
