from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('about/', views.about, name='users-about'),
    path('welcome/', views.welcome, name='users-welcome'),
    path('register/', views.register, name='users-register'),
    path('get_users/', views.get_users, name='users-get_users'),
    path('delete_user/', views.delete_user, name='users-delete_user'),
    path('update_user/', views.update_user, name='users-update_user'),
]
