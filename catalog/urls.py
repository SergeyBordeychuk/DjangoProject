from django.urls import path
from catalog.views import product_list, contacts, product_detail

app_name = 'catalog'

urlpatterns = [
    path('', product_list, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product'),
]