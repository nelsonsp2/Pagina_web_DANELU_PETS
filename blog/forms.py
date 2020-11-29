from .models import Domiciliario
from django import forms

class DomiciliarioCreate(forms.ModelForm):
    class Meta:
        model=Domiciliario
        fields='__all__'
