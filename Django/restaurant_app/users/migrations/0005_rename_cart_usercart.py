# Generated by Django 4.2.4 on 2023-08-24 07:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_remove_userorder_items_remove_userorder_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_userorder_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='UserCart',
        ),
    ]
