# Generated by Django 3.1.2 on 2020-10-14 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201009_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='addentional_images',
        ),
        migrations.CreateModel(
            name='ProductAdditionalImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addentional_images', models.ImageField(blank=True, null=True, upload_to='product_images_addentional', verbose_name='Дополнительные фотографии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_additional_images', to='product.product')),
            ],
        ),
    ]