from django.shortcuts import render, redirect
from .models import Tarea


def tareas(request):
    return render(request, 'tareas.html')


def crear_tarea(request):
    # Si es un método post, se intenta crear una tarea
    if request.method == "POST":
        # Se obtienen los datos del formulario y se guardan en variables
        # También se pueden pasar los datos del formulario directamente sin crear variables
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        es_importante = 'es_importante' in request.POST
        img = request.FILES.get('img')

        # Se pasan los valores para instanciar un nuevo objeto Tarea
        nueva_tarea = Tarea(
            usuario=request.user,
            titulo=titulo,
            descripcion=descripcion,
            es_importante=es_importante,
            img=img
        )

        # Un try para el manejo de errores
        try:
            nueva_tarea.save()

            return redirect('tareas')
        except Exception as e:
            return render(request, 'crear_tarea.html')

    # Si es un método get, se muestra el template
    return render(request, 'crear_tarea.html')
