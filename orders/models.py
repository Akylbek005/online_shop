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


class OrderProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата заказа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
