from django.http import Http404

from blog.models import Blog

from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name_blog', 'description', 'is_active']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog:home')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name_blog', 'description', 'is_active']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog:home')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'confirm_delete_blog.html'
    success_url = reverse_lazy('blog:home')


class ContactTemplateView(TemplateView):
    template_name = 'contacts_blog.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.count_views += 1
        obj.save()
        return obj


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        return queryset
