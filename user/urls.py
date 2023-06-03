from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view() , name='register'),
    path('login/', views.LoginView.as_view() , name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('active/<code>', views.ActiveUser.as_view(), name='active_user'),
]