
from django.db import models


# Create your models here.
class Cliente(models.Model):
    cédula = models.CharField(max_length=200, primary_key=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido= models.CharField(max_length=50)
    segundo_apellido= models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    dirección= models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)

    class Meta:
        ordering = ('-primer_nombre', '-primer_apellido')

    def __str__(self):
        return self.cédula


class Carrito(models.Model):
    id_carrito = models.CharField(max_length=200, primary_key=True)
    id_producto = models.CharField(max_length=200)
    cantidad_producto = models.SmallIntegerField()
    total_producto = models.IntegerField()
    id_cliente = models.ManyToManyField(Cliente)

    class Meta:
        ordering = ('-id_carrito', '-id_producto')

    def __str__(self):
        return self.id_carrito


class Cuenta(models.Model):
    numero_cuenta = models.CharField(max_length=200, primary_key=True)
    valor_total = models.IntegerField()
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-numero_cuenta', '-valor_total')

    def __str__(self):
        return self.id_carrito


class Domiciliario(models.Model):
    id_domiciliario = models.CharField(max_length=200, primary_key=True)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    medio_transporte = models.CharField(max_length=50)

    class Meta:
        ordering = ('-id_domiciliario', '-medio_transporte')

    def __str__(self):
        return self.id_domiciliario


class Domicilio(models.Model):
    id_domicilio = models.CharField(max_length=200, primary_key=True)
    id_domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    numero_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    metodo_de_pago = models.CharField(max_length=50)

    class Meta:
        ordering = ('-id_domicilio', '-id_domiciliario')

    def __str__(self):
        return self.id_domicilio


