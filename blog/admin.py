from django.contrib import admin
from .models import Cuenta
from .models import Carrito
from .models import Categoria
from .models import Cliente
from .models import Producto
from .models import Domicilio
from .models import Domiciliario
from .models import Admin
admin.site.register(Cuenta)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(Domiciliario)
admin.site.register(Admin)
admin.site.register(Domicilio)
# Register your models here.

