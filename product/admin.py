from django.contrib import admin
from django.contrib.admin import register

from product.models import Category, Brand, Product


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    prepopulated_fields = {
        'slug': ('title',)
    }


@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    prepopulated_fields = {
        'slug': ('title',)
    }


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'short_description',)
    list_editable = ('is_active',)
    prepopulated_fields = {
        'slug': ('title',)
    }