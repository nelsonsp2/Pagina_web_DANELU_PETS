from django.db import models

# Create your models here.

class Admin(models.Model):
    cedula_admin = models.CharField(max_length=11, primary_key=True)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)

    class Meta:
        ordering = ('-cedula_admin',)

    def __str__(self):
        return self.cedula_admin

class Categoria(models.Model):
    id_categoria = models.CharField(max_length=200, primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)

    class Meta:
        ordering = ('-especie',)

    def __str__(self):
        return self.especie

class Producto(models.Model):
    id_producto = models.CharField(max_length=200, primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    precio_producto = models.IntegerField()
    precio_produccion = models.IntegerField()
    picture = models.ImageField()
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    especificaciones = models.CharField(max_length=1000, default=None)
    admin_producto = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-precio_producto', '-nombre_producto')

    def __str__(self):
        return self.nombre_producto

