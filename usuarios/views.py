from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError


def inicio(request):
    return render(request, 'inicio.html')


def registrar(request):
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
            return render(request, 'incio.html', {
                'error': 'Usuario ya existente'
            })

    return render(request, 'inicio.html', {
        'error': 'Las contraseñas no coinciden'
    })


def iniciar_sesion(request):
    user = authenticate(
        request,
        username=request.POST['usuario'],
        password=request.POST['contra'],
    )

    if user is None:
        return render(request, 'inicio.html', {
            'error': 'Credenciales incorrectas'
        })
    else:
        login(request, user)

        return redirect('tareas')
