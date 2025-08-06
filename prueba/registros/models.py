from django.db import models
from ckeditor.fields import RichTextField

class Alumnos(models.Model):
    matricula = models.CharField(max_length=12, verbose_name="Matricula")
    nombre = models.TextField()
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    img = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True)
    
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    coment =RichTextField(verbose_name="Comentario")
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
        
    def __str__(self):
        return self.coment

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    
    class Meta:
        verbose_name = "Comentario de Contacto"
        verbose_name_plural = "Comentarios de Contacto"
        ordering = ['-created']
        
    def __str__(self):
        return self.mensaje
    
class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos",
    null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo