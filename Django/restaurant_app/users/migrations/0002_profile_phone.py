# Generated by Django 4.2.4 on 2023-08-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=1234567890, unique=True),
        ),
    ]
