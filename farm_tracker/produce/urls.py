# produce/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
   
]
