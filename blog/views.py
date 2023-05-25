from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 1


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'