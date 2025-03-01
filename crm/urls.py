"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

     path('', views.dashboard, name='dashboard'),

    path("customer/add/",views.CostumerView.as_view(),name="add"),

    path("customer/list/",views.CostumerListView.as_view(),name="list"),

    path("customer/detail/<int:pk>/",views.CostumerDetailView.as_view(),name="detail"),
    
    path("customer/<int:pk>/update",views.CustomerUpdateView.as_view(),name="update"),
    
    path("customer/delete/<int:pk>/",views.CustomerDeleteView.as_view(),name="delete"),
    


    
    path("register/",views.SignUpView.as_view(),name="signup"),

    path("login/",views.SignInView.as_view(),name="signin"),

    path("logout/",views.SignOutView.as_view(),name="logout")


    
]
