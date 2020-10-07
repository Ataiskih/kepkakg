# Generated by Django 3.1.2 on 2020-10-07 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('main_image', models.ImageField(default='', upload_to='', verbose_name='Основное фото')),
                ('addentional_images', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительные фотографии')),
                ('description', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Описание')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Старая цена')),
                ('new_price', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Новая цена')),
                ('cost_price', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Себестоимость')),
                ('quantity_in_warehouse', models.IntegerField(default=0, verbose_name='Колличество на на складе')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие в магазине')),
                ('shop', models.IntegerField(choices=[(1, 'ТЦ ЦУМ, 3 этаж, бутик B16'), (2, 'ТЦ Вефа, 1 этаж'), (3, 'Киевская, 124 (ориентрир ТЦ Караван)'), (4, 'г. Ош, ул. Масалиева, 44'), (5, 'Все магазины')], default=5, verbose_name='Магазины')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'товаров',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductCharacteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('material', models.CharField(blank=True, max_length=100, null=True, verbose_name='Материал')),
                ('size', models.IntegerField(choices=[(1, 'Extra Small - XS'), (2, 'Small - S'), (3, 'Medium - M'), (4, 'Large - L'), (5, 'Extra Large - XL'), (6, 'Double Large - XXL'), (7, 'Triple Large - XXXL')], default=1, verbose_name='Размеры')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characteristic', to='product.product')),
            ],
            options={
                'verbose_name': 'Характеристики товара',
                'verbose_name_plural': 'Характеристики товар',
                'ordering': ['name'],
            },
        ),
    ]
