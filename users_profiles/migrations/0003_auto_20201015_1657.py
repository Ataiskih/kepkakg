# Generated by Django 3.1.2 on 2020-10-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_profiles', '0002_auto_20201015_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Индекс'),
        ),
    ]
