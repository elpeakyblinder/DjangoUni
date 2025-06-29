from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as registros_views
from cursos import views as cursos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('contacto/',views.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('registros/', registros_views.registros, name="Registros"),
    path('cursos/', cursos_views.cursos, name="Cursos"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)