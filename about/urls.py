from django.urls import path

from about import views

urlpatterns = [
    path('', views.AboutUS.as_view(), name='about_us'),
]