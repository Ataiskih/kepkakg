# Generated by Django 3.1.2 on 2020-11-10 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201110_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item', to='order.orderlist'),
        ),
    ]
