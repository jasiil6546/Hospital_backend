# Generated by Django 5.1.1 on 2024-09-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=90)),
                ('PASSWORD', models.CharField(max_length=100)),
                ('EMAIL', models.EmailField(max_length=90)),
                ('PHONE_NUMBER', models.CharField(max_length=11)),
                ('CATEGORY', models.CharField(max_length=20)),
                ('AGE', models.PositiveIntegerField(max_length=200)),
                ('GENDER', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
