from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('setEmployeeData/', views.setEmployeeData, name='setEmployeeData'),
    path('getEmployeeData/', views.getEmployeeData, name='getEmployeeData'),
]
