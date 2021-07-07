from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available')
    list_display_links = ('name',)
    list_editable = ('price', 'available')
    search_fields = ('name',)
