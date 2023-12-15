from django.contrib import admin 
from django.urls import path 
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ourcats/', views.Catsview.as_view(), name='ourcats'),
    path('adoption', views.Adoption, name='adoption'),
    path('application', views.Application, name='application'),
     
]


