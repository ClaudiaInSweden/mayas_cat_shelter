from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home')
    path('cats', views.cats, name='cats')
    
]