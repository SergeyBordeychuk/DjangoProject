from django.shortcuts import render, get_list_or_404, get_object_or_404

from catalog.models import Product


def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, f'product_detail.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)
