# Generated by Django 3.1.2 on 2020-11-22 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20201122_0500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'Категории'},
        ),
    ]