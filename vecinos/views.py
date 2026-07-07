from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import RegistroVecinoForm
from .models import Vecino

def registro(request):
    if request.method == 'POST':
        form = RegistroVecinoForm(request.POST)
        if form.is_valid():
            # Guardar datos del vecino
            vecino = form.save(commit=False)
            vecino.rol = 'vecino'

            # Crear usuario de Django
            usuario = User.objects.create_user(
                username=form.cleaned_data['ci'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['nombre']
            )
            vecino.usuario = usuario
            vecino.save()

            messages.success(request, '¡Registro exitoso! Ya puedes iniciar sesión.')
            return redirect('inicio')
    else:
        form = RegistroVecinoForm()

    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # Verificar si es presidente
            try:
                vecino = Vecino.objects.get(usuario=user)
                if vecino.rol == 'presidente':
                    return redirect('dashboard')
            except Vecino.DoesNotExist:
                pass
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    messages.info(request, 'Sesión cerrada correctamente')
    return redirect('inicio')