from django.contrib import admin
from .models import Producto, ProductoCarrito, Carrito, Categoria
# Register your models here.


admin.site.register(Carrito)
admin.site.register(ProductoCarrito)
admin.site.register(Producto)
admin.site.register(Categoria)