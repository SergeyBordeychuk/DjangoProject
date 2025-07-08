from catalog.models import Product

from django.views.generic import DetailView, ListView, TemplateView


class ContactTemplateView(TemplateView):
    template_name = 'contacts_catalog.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
