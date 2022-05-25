from dataclasses import field
from django import forms

from .models import Plantilla

class PantillaFrom (forms.ModelForm):
    class Meta:
        model = Plantilla
        fields = ('posicion',)
    posicion = forms.CharField(max_length=200)

