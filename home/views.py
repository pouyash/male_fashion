from django.db.models import Count, Sum
from django.http import HttpRequest
from django.shortcuts import render

from product.models import Product
from site_settings.models import Slider


def home(request: HttpRequest):
    sliders = Slider.objects.filter(is_active=True)
    new_products = list(Product.objects.filter(is_active=True).order_by('-id'))[:12]
    most_sales = Product.objects.filter(is_active=True,order_detail__order__is_paid=True).annotate(sale_count=Sum('order_detail__count')).order_by("-sale_count")
    print(most_sales)

    context = {
        'sliders': sliders,
        'new_products': new_products,
        'most_sales': most_sales,
    }

    return render(request, 'main.html', context)


def header_component(request: HttpRequest):
    context = {}
    return render(request, 'layout/header_component.html', context)


def footer_component(request: HttpRequest):
    context = {}
    return render(request, 'layout/footer_component.html', context)
