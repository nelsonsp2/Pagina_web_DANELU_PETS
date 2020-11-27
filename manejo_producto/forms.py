from .models import Producto
from django import forms

class crear_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
