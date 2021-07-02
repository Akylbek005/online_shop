from django.contrib import admin
from .models import Product, OrderProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available')
    list_display_links = ('name',)
    list_editable = ('price', 'available')
    search_fields = ('name',)


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'product', 'created')
    list_display_links = ('name',)
    search_fields = ('name', 'email', 'product')
    list_filter = ('created',)
