# Generated by Django 5.1.1 on 2024-09-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_1', '0013_remove_doctors_password_remove_staffs_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='PASSWORD',
        ),
    ]
