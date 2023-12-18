from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cats/', views.cats, name='cats'),
    path('application/', views.application, name='application'),
]