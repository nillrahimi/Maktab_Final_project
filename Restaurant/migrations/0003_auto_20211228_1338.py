# Generated by Django 3.2.9 on 2021-12-28 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='manager_id',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='restaurant_id',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='branch_id',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='food_id',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderstatus_id',
            new_name='order_status',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
    ]
