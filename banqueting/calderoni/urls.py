from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modulo/', views.modulo, name='modulo'),
    path('login/', views.loginPage, name='loginPage'),
]
