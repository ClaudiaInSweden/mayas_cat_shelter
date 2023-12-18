from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cats/', views.cats, name='cats'),
    path('application/', views.application, name='application'),
    path('create-cat/', views.createCat, name='create-cat'),
    path('update-cat/<str:id>/', views.updateCat, name='update-cat'),
    path('delete-cat/<str:id>/', views.deleteCat, name='delete-cat'),
]