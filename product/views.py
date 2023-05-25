from django.db.models import QuerySet, Count, Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Product, Tag, Category, Brand


class ProductView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'products'
    paginate_by = 2
    ordering = '-id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data()
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all().annotate(count_product=Count('product'))
        context['brands'] = Brand.objects.all()
        return context

    def get_queryset(self):
        url = self.request.path
        slug = self.kwargs.get('slug')
        qs:QuerySet = super(ProductView, self).get_queryset()
        if 'category' in url:
            qs = qs.filter(category__slug=slug)
        elif 'brand' in url:
            qs = qs.filter(brand__slug=slug)
        elif 'tag' in url:
            qs = qs.filter(tag__slug=slug)

        return qs


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        product = kwargs.get('object')
        category = product.category.slug
        brand = product.brand.slug
        tag = list(product.tag_set.all())
        context['product_related'] = Product.objects.filter(Q(tag__in=tag) or Q(category__slug__iexact=category) or Q(brand__slug__iexact=brand)).exclude(id=product.id)

        return context
