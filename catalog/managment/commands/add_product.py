from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test products'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category = Category.objects.create(name_category = 'Games')

        products = [
            {'name_product': 'CS2', 'price': 880, 'category': category},
            {'name_product': 'Dota2', 'price': 0, 'category': category},
            {'name_product': 'CIV6', 'price': 3000, 'category': category},
        ]
        for product_data in products:
            product = Product.objects.create(**product_data)
