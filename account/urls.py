from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/',views.registrarCliente,name='registro'),
    path('register/',views.registerPage,name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboad, name='dashboard'),
    #path('', HomeView.as_view(), name='home'),
]