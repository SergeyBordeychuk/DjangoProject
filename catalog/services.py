from .models import Product
from django.core.cache import cache
from django.conf import settings

class ProductService:

    @staticmethod
    def get_products_from_cache():

        if not settings.CACHE_ENABLED:
            return Product.objects.all()

        key = 'product_list'
        products = cache.get(key)

        if products is not None:
            return products

        products = Product.objects.all()
        cache.set(key, products)
        return products
