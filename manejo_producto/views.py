from django.shortcuts import render, redirect
from .models import Producto
from .models import Categoria
from .models import Admin
from .forms import crear_producto
from django.http import HttpResponse


# Create your views here.
def estanteria(request):
    shelf = Producto.objects.all()
    return render(request, 'manejo_producto/tienda.html', {'tienda':shelf})
def publicar(request):
    upload = crear_producto()
    if request.method == 'POST':
        upload = crear_producto(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('estanteria')
        else:
            return HttpResponse('Su producto ingresado no es valido')
    else:
        return render(request, 'manejo_producto/modificar_producto.html', {'modificar_producto':upload})

def modificar (request, id_producto) :

    id_producto = int(id_producto)
    try:
        producto_buscar = Producto.objects.get(id = id_producto)
    except Producto.DoesNotExist:
        return redirect('estanteria')
    producto_form  = crear_producto(request.POST or None, instance= producto_buscar)

    if producto_form.is_valid():
        producto_form.save()
        return redirect('estanteria')
    return render(request, 'manejo_producto/modificar_producto.html', {'modificar_producto':producto_form})

def eliminar(request, id_producto):
    id_producto = int(id_producto)
    try:
        producto_buscar = Producto.objects.get(id = id_producto)
    except Producto.DoesNotExist:
        return redirect('estanteria')
    producto_buscar.delete()
    return redirect('estanteria')