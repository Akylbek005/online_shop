from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'available')
    date_hierarchy = 'created'

admin.site.register(Product, ProductAdmin)

