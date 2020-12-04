from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Categoria(models.Model):
    id_categoria = models.CharField(max_length=200, primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)

    class Meta:
        ordering = ('-especie',)

    def __str__(self):
        return self.especie


ETIQUETAS = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    precio_descuento = models.FloatField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    etiqueta = models.CharField(choices=ETIQUETAS, max_length=1)
    slug = models.SlugField()
    especificaciones = models.TextField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("carrito_compra:product", kwargs={
            'slug': self.slug
        })

    def get_agregar_al_carrito_url(self):
        return reverse("carrito_compra:agregar-al-carrito", kwargs={
            'slug': self.slug
        })

    def get_borrar_del_carrito_url(self):
        return reverse("carrito_compra:borrar-del-carrito", kwargs={
            'slug': self.slug
        })


class ProductoCarrito(models.Model):
    #usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    #orden = models.BooleanField(default=False)
    item = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} de {self.item.nombre}"


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductoCarrito)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_pedido = models.DateTimeField()
    orden = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario
