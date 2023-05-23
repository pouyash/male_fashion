from django.urls import path

from product import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('<slug>/', views.ProductDetail.as_view(), name='product'),
    path('category/<slug>/', views.ProductView.as_view(), name='product_by_category'),
    path('brand/<slug>/', views.ProductView.as_view(), name='product_by_brand'),
    path('tag/<slug>/', views.ProductView.as_view(), name='product_by_tag'),
]