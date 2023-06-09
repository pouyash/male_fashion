from django.urls import path

from account import views

urlpatterns = [
    path('', views.AccountMainView.as_view(), name='account_main'),
    path('change_password/', views.ChangePasswordEmail.as_view(), name='change_password_email'),
    path('change_password/<code>', views.Change_password.as_view(), name='change_password'),
    path('change_password_post/', views.Change_password_post.as_view(), name='change_password_post'),

    path('blogs/', views.BlogsListView.as_view(), name='account_blogs'),
    path('blogs/add/', views.BlogAddView.as_view(), name='account_blogs_add'),
    path('blogs/edit/<id>', views.BlogEditView.as_view(), name='account_blogs_edit'),
    path('blogs/delete/<pk>', views.DeleteBlogView.as_view(), name='account_blogs_delete'),
]
