# Generated by Django 5.0.1 on 2024-02-03 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_registration_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
    ]
