# Generated by Django 3.2 on 2021-05-31 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffeecat', '0003_customer_productorder_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coffeecat.customer'),
        ),
    ]
