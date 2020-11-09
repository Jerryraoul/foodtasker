"""foodtasker URL Configuration

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
from foodtaskerapp.views import Home, RestaurantHp, UserLogin, UserLogout, RestaurantSignup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('restaurant/',RestaurantHp, name='restaurant_home'),
    path('login/',UserLogin.as_view(), name='login_form'),
    path('logout/',UserLogout, name='logout'),
    path('restaurant/sign_up',RestaurantSignup, name='restaurant_signup'),
]
