from django.urls import path

from product import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('<slug>', views.ProductDetail.as_view(), name='product'),
]