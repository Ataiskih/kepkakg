from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from base.models import BaseAbstractModel
from autoslug import AutoSlugField
User = get_user_model()

from order.models import Customer

from order.models import Customer

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profile',
        verbose_name='Профиль',
    )
    avatar = models.ImageField(
        upload_to='user_profiles',
        default='user_profiles/devault_avatar.jpg/',
        verbose_name='Аватарка',
    )
    GENDER_CHOISE = (
        ('М', 'Мужчина'),
        ('Ж','Женщина'),
    )
    gender = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=GENDER_CHOISE,
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Телефон',
    )
    CHOISES = (
        ('Бишкек','Бишкек'),
        ('Ош','Ош'),
        ('Нарын','Нарын'),
        ('Баткен',''),
        ('Балыкчы','Балыкчы'),
        ('Талас','Талас'),
        ('Джалал-Абад','Джалал-Абад'),
    )
    address_city = models.CharField(
        max_length=50,
        choices=CHOISES,
        default='Бишкек',
    )
    zip_code = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name='Индекс',
    )
    address_optoinaly = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Дополнительный адрес',
    )
    slug = AutoSlugField(
        populate_from='user',
        default='user',
    )

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"


def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        print('customer created')

post_save.connect(create_customer, sender=User)

def update_customer(sender, instance, created, **kwargs):
    if created == False:
        instance.customer.save()
        print('customer updated')

post_save.connect(update_customer, sender=User)