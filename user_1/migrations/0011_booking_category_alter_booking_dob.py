# Generated by Django 5.1.1 on 2024-09-22 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_1', '0010_doctors_user_name_patients_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='CATEGORY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DOB',
            field=models.DateTimeField(blank=True, max_length=100, null=True),
        ),
    ]
