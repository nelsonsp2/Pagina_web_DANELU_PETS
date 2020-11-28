from django.contrib import admin

from .models import Carrito
from .models import Cliente
from .models import Cuenta
from .models import Domicilio
from .models import Domiciliario
from manejo_producto.models import Admin

# Register your models here.
admin.site.register(Admin)
admin.site.register(Carrito)
admin.site.register(Cliente)
admin.site.register(Cuenta)

admin.site.register(Domiciliario)
admin.site.register(Domicilio)


