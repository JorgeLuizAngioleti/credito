"""treino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from app1.views import home, AddEntrada, AddSaida, boasvindas, capa, register_request, logout1
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', boasvindas, name='url_boasvindas'),
    path("logout/", logout1, name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('home/', home, name='url_home'),
    path('capa/', capa, name='url_capa'),
    path('Entradas/', AddEntrada, name='url_entrada'),
    path('Saidas/', AddSaida, name='url_saida'),
    path("register/", register_request, name="register"),
]
