"""
URL configuration for wasteproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    

    #user
    path('user_registration/', views.user_registration,name='user_registration'),
    path('user_login/', views.user_login,name='user_login'),
    path('user_home/', views.user_home,name='user_home'),
    path('user_profile/', views.user_profile,name='user_profile'),
    path('user_update/',views.user_update,name='user_update'),
    path('proupdate/', views.proupdate,name='proupdate'),
    path('delete_ac/',views.delete_ac,name='delete_ac'),
    path('upload_waste/',views.upload_waste,name='upload_waste'),



    #admin
    path('admin_login/', views.admin_login,name='admin_login'),
    path('admin_home/', views.admin_home,name='admin_home'),
    path('user_list/', views.user_list,name='user_list'),
    path('delete_user/<int:id>', views.delete_user,name='delete_user'),
]
