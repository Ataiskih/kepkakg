# Generated by Django 3.1.2 on 2020-11-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_shipping_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
