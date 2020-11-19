from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class FeedBack(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    name = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name="Ваше имя"
    )

    text = models.TextField(
        null=True, blank=True,
        verbose_name="Текст обращения"
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    phone = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name="Телефон"
    )

    email = models.EmailField(
        max_length=255,
        null=True, blank=True,
        verbose_name="Электронная почта"
    )

    answer = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Формы обратной связи"
