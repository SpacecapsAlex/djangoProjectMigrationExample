# Generated by Django 4.2.7 on 2023-11-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_is_programmer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_programmer',
            field=models.BooleanField(default=False),
        ),
    ]