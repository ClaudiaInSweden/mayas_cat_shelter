from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('cats/', views.cats),
    path('apply/', views.apply),
]