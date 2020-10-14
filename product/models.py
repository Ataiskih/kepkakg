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


class Product(BaseAbstractModel):
    main_image = models.ImageField(
        default='/product_images_main/default_main_photo.png/',
        upload_to='product_images_main',
        verbose_name='Основное фото'
    )
    vendor_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Артикул'
    )
    description = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    old_price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name='Текущая цена'
    )
    new_price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name='Новая цена'
    )
    cost_price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name='Себестоимость'
    )
    quantity_in_warehouse = models.IntegerField(
        default=0,
        verbose_name='Колличество на на складе'
    )
    availability = models.BooleanField(
        default=True,
        verbose_name='Наличие в магазине'
    )
    SHOPS = (
        (1, 'ТЦ ЦУМ, 3 этаж, бутик B16'),
        (2, 'ТЦ Вефа, 1 этаж'),
        (3, 'Киевская, 124 (ориентрир ТЦ Караван)'),
        (4, 'г. Ош, ул. Масалиева, 44'),
        (5, 'Все магазины')
    )
    shop = models.IntegerField(
        choices=SHOPS,
        default=5,
        verbose_name='Магазины'
    )


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProductAdditionalImages(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_additional_images'
    )
    addentional_images = models.ImageField(
        null=True,
        blank=True,
        upload_to='product_images_addentional',
        verbose_name='Дополнительные фотографии'
    )


class ProductCharacteristic(models.Model):
        product = models.ForeignKey(
            Product,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name='characteristic'
        )
        material = models.CharField(
            max_length=100,
            null=True,
            blank=True,
            verbose_name='Материал'
        )
        CHOOSE_SIZE = (
            (1, 'XS'),
            (2, 'S'),
            (3, 'M'),
            (4, 'L'),
            (5, 'XL'),
            (6, 'XXL'),
            (7, 'XXXL'),
            (8, 'Все размеры XS - XXXL'),
        )
        size = models.IntegerField(
            choices=CHOOSE_SIZE,
            default=8,
            verbose_name='Размеры'
        )
        color = models.CharField(
            max_length=100,
            null=True,
            blank=True,
            verbose_name='Цвет'
        )


        class Meta:
            verbose_name = "Характеристики товара"
            verbose_name_plural = "Характеристики товаров"

