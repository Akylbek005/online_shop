from django.db import models

from products.models import Products
from users.models import User


class Orders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, null=True, blank=True, related_name='products')

    def __str__(self):
        return f'{self.user}, {self.products}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
