from django.contrib import admin
from .models import Curso
from .models import Actividad


class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'costo', 'duracion_horas', 'publicado', 'created')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'created'
    list_filter = ('publicado', 'created')

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso', 'created')
    list_filter = ('curso',)
    search_fields = ('descripcion', 'curso_nombre')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated', 'id')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Actividad, ActividadAdmin)