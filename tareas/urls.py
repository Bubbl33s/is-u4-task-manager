from django.urls import path
from . import views

urlpatterns = [
    path('', views.tareas, name='tareas'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('actualizar_tarea/<int:tarea_id>',
         views.actualizar_tarea, name='actualizar_tarea'),
    path('eliminar_tarea/<int:tarea_id>',
         views.eliminar_tarea, name='eliminar_tarea'),
]
