from django import forms
from cursos.models import Interfaz

class InterfazForm(forms.ModelForm):
    class Meta:
        model = Interfaz
        fields = (
            'curso',
            'description',
            'document',
            'photo',
        )