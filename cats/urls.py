from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cats/', views.cats, name='cats'),
    path('adoption/', views.adoption, name='adoption'),
    path('create-cat/', views.createCat, name='create-cat'),
    path('update-cat/<str:pk>/', views.updateCat, name='update-cat'),
    path('delete-cat/<str:pk>/', views.deleteCat, name='delete-cat'),
    path('rules/', views.rules, name='rules'),
    path('administration/', views.administration, name='administration')
]