from django import forms
from django.contrib.auth.models import User
from .models import Vecino

class RegistroVecinoForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control-modern',
            'placeholder': 'Ingresa tu contraseña'
        }),
        label='Contraseña'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control-modern',
            'placeholder': 'Confirma tu contraseña'
        }),
        label='Confirmar contraseña'
    )

    class Meta:
        model = Vecino
        fields = ['nombre', 'ci', 'direccion', 'telefono', 'barrio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control-modern',
                'placeholder': 'Ej: Juan Pérez'
            }),
            'ci': forms.TextInput(attrs={
                'class': 'form-control-modern',
                'placeholder': 'Ej: 12345678'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control-modern',
                'placeholder': 'Ej: Calle Sucre #123'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control-modern',
                'placeholder': 'Ej: 71234567'
            }),
            'barrio': forms.TextInput(attrs={
                'class': 'form-control-modern',
                'placeholder': 'Ej: Loma Suárez'
            }),
        }

    def clean_ci(self):
        ci = self.cleaned_data.get('ci')
        if Vecino.objects.filter(ci=ci).exists():
            raise forms.ValidationError('Este CI ya está registrado')
        return ci

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return cleaned_data