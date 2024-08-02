from django.urls import path
from . import views

urlpatterns = [
    path('', views.tareas, name='tareas'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
]
