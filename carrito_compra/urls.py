from django.urls import path
from .views import (HomeView, checkout, ProductDetailView, agregar_al_carrito, borrar_del_carrito)


app_name = 'carrito_compra'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('agregar-al-carrito/<slug>/', agregar_al_carrito, name='agregar-al-carrito'),
    path('borrar-del-carrito/<slug>/', borrar_del_carrito, name='borrar-del-carrito')

]
