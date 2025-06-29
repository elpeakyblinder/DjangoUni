from django.db import models
from django.utils import timezone # manejar las fechas y horas de una manera que no dependa de la ubicación geográfica del servidor o del usuario
from ckeditor.fields import RichTextField

class Curso(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Título del Curso")
    descripcion = RichTextField(verbose_name="Descripción Detallada")
    duracion_horas = models.IntegerField(verbose_name="Duración (en horas)")
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Costo de Inscripción (MXN)")
    publicado = models.BooleanField(default=False, verbose_name="¿Está publicado?")
    imagen = models.ImageField(upload_to='cursos/imagenes/', null=True, blank=True, verbose_name="Imagen Promocional")
    created = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre