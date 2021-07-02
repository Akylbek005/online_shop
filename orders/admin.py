from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'status', 'available')
    list_display_links = ('name',)
    list_filter = ('status',)
    list_editable = ('price', 'status', 'available')
    search_fields = ('name',)
