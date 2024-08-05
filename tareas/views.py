from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Tarea


@login_required
def tareas(request):
    tareas = Tarea.objects.all().filter(usuario=request.user)

    return render(request, 'tareas.html', {
        'tareas': tareas
    })


@login_required
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


@login_required
def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    return render(request, 'detalle_tarea.html', {
        'tarea': tarea,
    })


@login_required
def actualizar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    # Datos actualizados
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    es_importante = 'es_importante' in request.POST

    tarea.titulo = titulo
    tarea.descripcion = descripcion
    tarea.es_importante = es_importante
    # Verificar si se ha subido una nueva imagen
    if 'img' in request.FILES:
        tarea.img = request.FILES['img']

    # Un try para el manejo de errores
    try:
        tarea.save()

        return redirect('tareas')
    except Exception as e:
        return render(request, 'detalle_tarea.html')


@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    if request.method == 'POST':
        tarea.delete()

        return redirect('tareas')


@login_required
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)

    if request.method == 'POST':
        tarea.fecha_completada = timezone.now()
        tarea.save()

        return redirect('tareas')
