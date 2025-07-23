from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product

from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    template_name = 'confirm_delete_catalog.html'
    success_url = reverse_lazy('catalog:home')


class ContactTemplateView(TemplateView):
    template_name = 'contacts_catalog.html'


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
