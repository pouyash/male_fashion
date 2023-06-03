from django.urls import path

from order import views

urlpatterns = [
    path('', views.OrderView.as_view(), name='order'),
    path('add-to-card/<slug>/', views.AddToCardView.as_view(), name='add_to_card'),
    path('remove-from-card/<id>/', views.remove, name='remove_from_card'),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]