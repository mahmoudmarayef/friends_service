# Generated by Django 4.2.1 on 2023-05-08 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0009_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]