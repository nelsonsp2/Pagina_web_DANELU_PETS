from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm , CreateUserForm, CreateClienteform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Cliente


#------------------------------------
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('carrito_compra:home')
                else:
                    return redirect('registro')
            else:
                return redirect('registro')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboad(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Hola"+user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)

def registrarCliente (request):
    form = CreateClienteform()
    if request.method == 'POST':
        form = CreateClienteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            return HttpResponse('Algo salio mal')
    else:
        context = {'form': form}
        return render(request, 'account/registro.html', context)


