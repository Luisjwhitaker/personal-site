# Generated by Django 3.2 on 2021-06-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeecat', '0010_rename_orders_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='coffeecat.CartItem'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]