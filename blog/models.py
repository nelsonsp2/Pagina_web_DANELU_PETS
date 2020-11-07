from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Admin(models.Model):
    cedula_admin = models.CharField(max_length=11, primary_key= True)
    Nombre1 = models.CharField(max_length= 50)
    Nombre2 = models.CharField(max_length= 50)
    Apellido1 = models.CharField(max_length= 50)
    Apellido2 = models.CharField(max_length= 50)

    class Meta:
        ordering = ('-cedula_admin',)

    def __str__(self):
        return self.cedula_admin

class Categoria(models.Model):
    id_categoria = models.CharField(max_length= 200, primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)

    class Meta:
        ordering = ('-especie',)

    def __str__(self):
        return self.especie
class Producto(models.Model):
    id_producto = models.CharField(max_length=200,primary_key= True)
    nombre_producto = models.CharField(max_length=200)
    precio_producto = models.IntegerField()
    precio_produccion = models.IntegerField()
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    admin_producto = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-precio_producto', '-nombre_producto')

    def __str__(self):
        return self.nombre_producto
class Cliente(models.Model):
    id_cliente = models.CharField(max_length=200,primary_key= True)
    Nombre1 = models.CharField(max_length=50)
    Nombre2 = models.CharField(max_length=50)
    Apellido1 = models.CharField(max_length=50)
    Apellido2 = models.CharField(max_length=50)
    Correo= models.EmailField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=50)

    class Meta:
        ordering = ('-Nombre1', '-Apellido1')

    def __str__(self):
        return self.id_cliente

class Carrito(models.Model):
    id_carrito = models.CharField(max_length=200, primary_key= True)
    id_producto = models.CharField(max_length=200, primary_key=True)
    cantidad_producto = models.SmallIntegerField()
    total_producto = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id_carrito', '-id_producto')

    def __str__(self):
        return self.id_carrito

class Cuenta(models.Model):
    numero_cuenta = models.CharField(max_length=200, primary_key= True)
    valor_total = models.IntegerField()
    id_carrito = models.ForeignKey(Carrito, on_delete= models.CASCADE)
    class Meta:
        ordering = ('-numero_cuenta', '-valor_total')

    def __str__(self):
        return self.id_carrito

