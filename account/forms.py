from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  .models import Cliente


class CreateClienteform(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']