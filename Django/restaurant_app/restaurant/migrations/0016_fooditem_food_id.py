# Generated by Django 4.2.4 on 2023-08-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_remove_userorder_items_remove_userorder_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='food_id',
            field=models.CharField(default='1', max_length=100, unique=True),
        ),
    ]
