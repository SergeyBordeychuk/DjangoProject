from django.contrib import admin
from catalog.models import Product, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name_product', 'description')
