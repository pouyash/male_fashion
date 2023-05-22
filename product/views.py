from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Product


class ProductView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'products'
    paginate_by = 2
    ordering = '-id'



class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

