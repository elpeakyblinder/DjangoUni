from django.contrib import admin
from .models import Alumnos
from .models import Comentario

class AdministradorModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'img')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno', 'img')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
    
admin.site.register(Alumnos, AdministradorModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    
admin.site.register(Comentario, AdministrarComentarios)