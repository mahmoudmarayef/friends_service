# Generated by Django 4.2.1 on 2023-05-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0012_friendship_delete_friendrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
