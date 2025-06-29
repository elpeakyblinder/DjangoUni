from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'costo', 'duracion_horas', 'publicado', 'created')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'created'
    list_filter = ('publicado', 'created')

admin.site.register(Curso, CursoAdmin)