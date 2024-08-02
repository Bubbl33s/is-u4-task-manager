from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_completada = models.DateTimeField(null=True, blank=True)
    es_importante = models.BooleanField(default=False)
    img = models.ImageField(upload_to='tareas_imgs/', blank=True)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.usuario.username}"
