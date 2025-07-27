from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View

from catalog.forms import ProductForm
from catalog.models import Product

from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
