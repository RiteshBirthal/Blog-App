# Generated by Django 4.2.4 on 2023-08-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_usercart_food_item_usercart_food_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='food_image_url',
            field=models.CharField(default='', max_length=500),
        ),
    ]
