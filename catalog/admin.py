from django.contrib import admin

from catalog.models import Category, Product, Contact, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('num', 'name', 'is_active',)