# Generated by Django 5.1.1 on 2024-09-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=90)),
                ('PASSWORD', models.CharField(max_length=90)),
                ('EMAIL', models.EmailField(max_length=50)),
                ('PHONE_NUMBER', models.CharField(max_length=11)),
                ('CATEGORY', models.CharField(max_length=200)),
                ('AGE', models.PositiveIntegerField()),
                ('GENDER', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
