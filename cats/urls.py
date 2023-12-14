from django.contrib import admin 
from django.urls import path 
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cats/', views.Cats, name='cats'),
    path('adoption/', views.adoption, name='adoption')
     
]


