# Generated by Django 5.1.1 on 2024-09-22 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_1', '0008_registrationform_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='CATEGORY',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='PASSWORD',
        ),
        migrations.AddField(
            model_name='booking',
            name='DOB',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
