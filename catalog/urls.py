from django.urls import path
from catalog.views import ProductListView, ContactTemplateView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, UnpublishProductView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('unpublish/<int:pk>/', UnpublishProductView.as_view(), name='unpublish'),
]