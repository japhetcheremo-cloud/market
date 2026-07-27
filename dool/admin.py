from django.contrib import admin
from .models import Product, Cart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'featured',
        'created_at',
    )

    list_filter = (
        'featured',
        'category',
    )

    search_fields = (
        'name',
        'description',
        'category',
    )

    ordering = (
        '-created_at',
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'product',
        'quantity',
        'added_at',
    )

    search_fields = (
        'user__username',
        'product__name',
    )

    ordering = (
        '-added_at',
    )