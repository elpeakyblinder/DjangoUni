from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as registros_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registros_views.principal, name="Principal"),
    path('contacto/',registros_views.contacto, name="Contacto"),
    path('formulario/', registros_views.formulario, name="Formulario"),
    path('registros/', registros_views.registros, name="Registros"),
    path('registrar/', registros_views.registrar, name= "Registrar"),
    path('comentario/', registros_views.comentario, name="Comentario"),
    path('eliminarComentario/<int:id>/',registros_views.eliminarComentarioContacto, name='Eliminar'),
    path('formEditarComentario/<int:id>/',registros_views.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', registros_views.editarComentarioContacto, name='Editar'),
    path('consultas1/', registros_views.consultar1, name='Consultas'),
    path('consultas2/', registros_views.consultar2, name='Consultas'),
    path('consultas3/', registros_views.consultar3, name='Consultas'),
    path('consultas4/', registros_views.consultar4, name='Consultas'),
    path('consultas5/', registros_views.consultar5, name='Consultas'),
    path('consultas6/', registros_views.consultar6, name='Consultas'),
    path('consultas7/', registros_views.consultar7, name='Consultas'),
    path('consulta_por_fecha/', registros_views.consulta_por_fecha, name='Consultas'),
    path('consulta_por_expresion/', registros_views.consulta_por_expresion, name='Consultas'),
    path('consulta_por_usuario/', registros_views.consulta_por_usuario, name='Consultas'),
    path('consulta_solo_mensajes/', registros_views.consulta_solo_mensajes, name='Consultas'),
    path('consulta_expresion_diferente/', registros_views.consulta_expresion_diferente, name='Consultas'),
    path('subir',registros_views.archivos, name="Subir"),
    path('consultasSQL',registros_views.consultasSQL,name="sql"),
    path('seguridad/', registros_views.seguridad, name='Seguridad'),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)