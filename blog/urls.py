from django.urls import path
from blog.views import BlogDetailView, BlogListView, ContactTemplateView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]