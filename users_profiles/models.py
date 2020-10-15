from django.db import models
from django.contrib.auth import get_user_model
from base.models import BaseAbstractModel
User = get_user_model()


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


    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
