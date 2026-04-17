from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "seller", "category", "price", "status", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "slug", "short_description")
    prepopulated_fields = {"slug": ("title",)}