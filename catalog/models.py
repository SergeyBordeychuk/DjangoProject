from django.db import models

from users.models import CustomUser


# Create your models here.

class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Продукт')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    is_publicate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', help_text='Укажите владельца продукта', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
