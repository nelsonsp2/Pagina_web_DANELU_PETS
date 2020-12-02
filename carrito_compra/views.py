from django.shortcuts import render, get_object_or_404
from .models import Producto, Carrito, ProductoCarrito
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
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


#funcion para agegar elementos al carrito, primero revisa si la
#pedido no esta activo antes de agregar elementos a el


def agregar_al_carrito(request, slug):
    item = get_object_or_404(Producto, slug=slug)
    producto_carrito = ProductoCarrito.objects.create(item=item)
    pedido_qs = Carrito.objects.filter(usuario=request.user.username, orden=False)
    if pedido_qs.exists():
        pedido = pedido_qs[0]
        #revisamos si el producto a agregar ya esta en el pedido
        if pedido.items.filter(item__slug=item.slug).exists():
            producto_carrito.cantidad += 1
            producto_carrito.save()
    else:
        #fecha_pedido = timezone.now()
        pedido = Carrito.objects.create(usuario=request.user.username)
        pedido.items.add(producto_carrito)
    return redirect("carrito_compra:product", kwargs={
        'slug': slug
    })
