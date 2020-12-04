from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    cédula = models.CharField(max_length=200, primary_key=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    dirección = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)

    class Meta:
        ordering = ('-primer_nombre', '-primer_apellido')

    def __str__(self):
        return self.cédula


