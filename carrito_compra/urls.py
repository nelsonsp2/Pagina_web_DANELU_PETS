from django.urls import path
from .views import (HomeView, checkout, ProductDetailView, agregar_al_carrito)


app_name = 'carrito_compra'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', agregar_al_carrito, name='add-to-cart')

]
