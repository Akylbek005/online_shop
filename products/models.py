from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=124, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='product/image', verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
