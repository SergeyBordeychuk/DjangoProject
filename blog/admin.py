from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_blog', 'is_active',)
    search_fields = ('name_blog', 'description')
