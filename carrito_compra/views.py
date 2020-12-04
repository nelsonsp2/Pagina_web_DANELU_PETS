from django.shortcuts import render, get_object_or_404
from .models import Producto, Carrito, ProductoCarrito
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages


# Create your views here.


def products(request):
    context = {
        'items': Producto.objects.all()
    }
    return render(request, "product.html", context)


def checkout(request):
    return render(request, "checkout.html")


class HomeView(ListView):
    model = Producto
    template_name = "home.html"


class ProductDetailView(DetailView):
    model = Producto
    template_name = "product.html"


# funcion para agegar elementos al carrito, primero revisa si la
# pedido no esta activo antes de agregar elementos a el


def agregar_al_carrito(request, slug):
    item = get_object_or_404(Producto, slug=slug)
    producto_carrito = ProductoCarrito.objects.create(item=item)
    # producto_carrito, created = ProductoCarrito.objects.get_or_create(item=item, usuario=request.user, orden =False)
    pedido_qs = Carrito.objects.filter(usuario=request.user, orden=False)
    if pedido_qs.exists():
        pedido = pedido_qs[0]
        # revisamos si el producto a agregar ya esta en el pedido
        if pedido.items.filter(item__slug=item.slug).exists():
            producto_carrito.cantidad += 1
            producto_carrito.save()
            messages.info(request, "Este producto fue actualizado en tu carrito.")
            return redirect("carrito_compra:product", slug=slug)
        else:
            pedido.items.add(producto_carrito)
            messages.info(request, "Este producto fue agregado a tu carrito.")
            return redirect("carrito_compra:product", slug=slug)
    else:
        fecha_pedido = timezone.now()
        pedido = Carrito.objects.create(usuario=request.user, fecha_pedido=fecha_pedido)
        pedido.items.add(producto_carrito)
        messages.info(request, "Este producto fue agregado a tu carrito.")
        return redirect("carrito_compra:product", slug=slug)

    return redirect("carrito_compra:product", slug=slug)


# funcion de borrado de elementos del carrito
def borrar_del_carrito(request, slug):
    item = get_object_or_404(Producto, slug=slug)
    # producto_carrito, created = ProductoCarrito.objects.get_or_create(item=item, usuario=request.user, orden =False)
    pedido_qs = Carrito.objects.filter(usuario=request.user.pk, orden=False)
    if pedido_qs.exists():
        pedido = pedido_qs[0]
        # revisamos si el producto a agregar ya esta en el pedido
        if pedido.items.filter(item__slug=item.slug).exists():
            producto_carrito = ProductoCarrito.objects.create(item=item)[0]
            # producto_carrito, created = ProductoCarrito.objects.get_or_create(item=item, usuario=request.user, orden =False)[0]
            pedido.items.remove(producto_carrito)
            messages.info(request, "Este producto fue removido de tu carrito.")
            return redirect("carrito_compra:product", slug=slug)
        else:
            messages.info(request, "Este producto no se encontraba en tu carrito.")
            return redirect("carrito_compra_product", sulg=slug)
    else:
        messages.info(request, "Usted no tiene una orden activa.")
        return redirect("carrito_compra:product", slug=slug)

    # messages.info(request, "Usted no tiene una orden activa.")
    return redirect("carrito_compra:product", slug=slug)
