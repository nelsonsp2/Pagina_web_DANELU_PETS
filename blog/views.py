from django.shortcuts import render, redirect
from .models import Domiciliario
from .forms import DomiciliarioCreate
from django.http import HttpResponse
# Create your views here.

def index(request):
    shelf=Domiciliario.objects.all()
    return render (request, 'Domiciliario/library.html',{'shelf':shelf})

def upload(request):
    upload = DomiciliarioCreate()
    if request.method =='POST':
        upload = DomiciliarioCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('Los datos dados no son validos')
    else:
        return render(request, 'Domiciliario/upload_form.html',{'upload_form':upload})


def delete_Domiciliario(request, Domiciliario_id):
    Domiciliario_id = int(Domiciliario_id)
    try:
        Domiciliario_sel = Domiciliario.objects.get(id=Domiciliario_id)
    except Domiciliario.DoesNotExist:
        return redirect('index')
    Domiciliario_sel.delete()
    return redirect('index')

def update_Domiciliario(request, Domiciliario_id):
    Domiciliario_id=int(Domiciliario_id)
    try:
        Domiciliario_sel = Domiciliario.objects.get(id=Domiciliario_id)
    except Domiciliario.DoesNotExist:
        return  redirect('index')
    Domiciliario_form = DomiciliarioCreate(request.POST or None, instance=Domiciliario_sel)
    if Domiciliario_form.is_valid():
        Domiciliario_form.save()
        return redirect('index')
    return render(request, 'Domiciliario/upload_form.html',{'upload_form':Domiciliario_form})


