# Generated by Django 4.2.4 on 2023-08-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_fooditem_food_id'),
        ('users', '0007_usercart_food_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='items',
            field=models.ManyToManyField(to='restaurant.food'),
        ),
    ]
