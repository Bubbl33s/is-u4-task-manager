from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def inicio(request):
    # Se cierra la sesión para que no se muestre la navbar
    logout(request)

    return render(request, 'inicio.html')


def registrar(request):
    # Verifica que ambas contraseñas del formulario sean la misma
    if request.POST['contra1'] == request.POST['contra2']:
        try:
            user = User.objects.create_user(
                username=request.POST['usuario'],
                password=request.POST['contra1']
            )
            user.save()
            login(request, user)

            return redirect('tareas')

        except IntegrityError:
            # Maneja el error de usuario duplicado
            return render(request, 'incio.html', {
                'error': 'Usuario ya existente'
            })

    # Si las contraseñas no coinciden, regresa al inicio
    return render(request, 'inicio.html', {
        'error': 'Las contraseñas no coinciden'
    })


def iniciar_sesion(request):
    # Verifica las credenciales ingresadas
    user = authenticate(
        request,
        username=request.POST['usuario'],
        password=request.POST['contra'],
    )

    # Si no se encontró un usuario no se inicia sesión
    if user is None:
        messages.error(request, 'Credenciales incorrectas')

        return render(request, 'inicio.html')
    # Si las credenciales son correctas, se redirije a la página de tareas
    else:
        login(request, user)
        messages.success(request, f"Bienvend@ {user.username}")

        return redirect('tareas')


@login_required
def cerrar_sesion(request):
    logout(request)

    return redirect('inicio')
