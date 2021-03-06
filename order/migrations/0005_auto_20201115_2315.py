# Generated by Django 3.1.2 on 2020-11-15 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20201014_1826'),
        ('order', '0004_auto_20201110_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order_list',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='order_list',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.customer'),
        ),
        migrations.DeleteModel(
            name='OrderList',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order'),
        ),
        migrations.AddField(
            model_name='shipping',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order'),
        ),
    ]
