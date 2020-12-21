"""Dialectic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dialecticapp import views

urlpatterns = [
    path('',views.dialectic_home, name='home'),
    path('login/', views.dialectic_signIn, name='login'),
    path('join/', views.dialectic_signUp, name='join'),
    path('table/', views.dialectic_schedule, name='table'),
    path('update/<str:pk>/', views.dialectic_update, name='update'),
]
