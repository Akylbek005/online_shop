from django.contrib import admin
from .models import Product
<<<<<<< HEAD


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'status', 'available')
    list_display_links = ('name',)
    list_filter = ('status',)
    list_editable = ('price', 'status', 'available')
    search_fields = ('name',)
=======

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'available')
    date_hierarchy = 'created'

admin.site.register(Product, ProductAdmin)

>>>>>>> db132f59df7cba061961621f8796fc12538a99e2
