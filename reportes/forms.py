from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['tipo', 'descripcion', 'ubicacion', 'latitud', 'longitud', 'foto']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control-modern',
                'placeholder': 'Describe el problema con detalle...'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control-modern',
                'placeholder': 'Ej: Calle Sucre entre 6 de Agosto y Bolívar',
                'style': 'width: 100%;'
            }),
            'latitud': forms.HiddenInput(attrs={
                'id': 'id_latitud'
            }),
            'longitud': forms.HiddenInput(attrs={
                'id': 'id_longitud'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control-modern'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control-modern',
                'accept': 'image/*'
            }),
        }
