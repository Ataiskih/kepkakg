from django.db import models


class BaseAbstractModel(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Название'
    )
    created = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    deleted = models.BooleanField(
        default=False,
        verbose_name='Удален'
    )

    def __str__(self):
        if self.name:
            return self.name
        return f"{self.pk}"

    class Meta:
        abstract = True