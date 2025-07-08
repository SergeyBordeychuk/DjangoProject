from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
