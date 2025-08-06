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
    
class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave de la Actividad")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso al que Pertenece")
    descripcion = RichTextField(config_name='actividad_editor', verbose_name="Descripción de la Actividad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['-created']

    def __str__(self):
        return self.descripcion