from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto


class AdministradorModelo(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("matricula", "nombre", "carrera", "turno", "img")
    search_fields = ("matricula", "nombre", "carrera", "turno")
    date_hierarchy = "created"
    list_filter = ("carrera", "turno")

    list_per_page = 2
    list_display_links = ("matricula", "nombre")
    list_editable = ("turno",)

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="UsuariosDelete").exists():
            return (
                "created",
                "alumno",
            )
        else:
            return ("created",)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ("id", "coment", "alumno")
    search_fields = ("id", "created", "alumno__nombre")
    date_hierarchy = "created"
    readonly_fields = ("created", "id")

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ("created", "updated", "matricula", "carrera", "turno")
        else:
            return ("created", "updated")


class AdministrarComentariosContacto(admin.ModelAdmin):
    # CORRECCIÓN: Se cambió 'create' a 'created' para que coincida con el modelo
    list_display = ("id", "mensaje", "created")
    search_fields = ("id", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "id")


admin.site.register(Comentario, AdministrarComentarios)
admin.site.register(Alumnos, AdministradorModelo)
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
