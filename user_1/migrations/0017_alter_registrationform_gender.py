# Generated by Django 5.1.1 on 2024-09-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_1', '0016_rename_token_booking_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='GENDER',
            field=models.CharField(max_length=200),
        ),
    ]
