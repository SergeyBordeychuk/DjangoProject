from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category

from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .services import ProductService


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('product.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для снятия продукта.")

        product.is_publicate = False
        product.save()

        return redirect('catalog:product', pk=product_id)


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Product
    template_name = 'confirm_delete_catalog.html'
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'


class ContactTemplateView(TemplateView):
    template_name = 'contacts_catalog.html'


@method_decorator(cache_page(60*15), name='dispatch')
class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductService.get_products_from_cache()


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'products'


    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Product.objects.filter(category_name__id=pk)


class CategoryCreateView(CreateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('catalog:category_list')
