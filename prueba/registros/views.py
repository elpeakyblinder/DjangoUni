from django.shortcuts import render, redirect
from .models import Alumnos, Archivos
from .forms import ComentarioContactoForm, FormArchivos
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages

def principal(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {"alumnos": alumnos})

def registros(request):
    lista_alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {"alumnos": lista_alumnos})

def formulario(request):
    return render(request, "registros/formulario.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return redirect('Comentario')
    form = ComentarioContactoForm()
    return render(request,'registros/registrar.html',{'form': form})

def contacto(request):
    return render(request,"registros/contacto.html")
    
def comentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id): 
    # Buscamos el comentario por su ID, si no existe, dará un error 404
    comentario = get_object_or_404(ComentarioContacto, id=id)
    
    if request.method == 'POST':
        comentario.delete()
        # Redireccionamos a la lista de comentarios después de borrar
        return redirect('Comentario')
        
    # Si el método es GET, mostramos la página de confirmación
    return render(request, 'registros/confirmarEliminacion.html', {'object': comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.

def editarComentarioContacto(request, id):
    # Buscamos el comentario que se va a editar
    comentario = get_object_or_404(ComentarioContacto, id=id)
    
    if request.method == 'POST':
        # Si el formulario se envía, lo procesamos con los datos nuevos
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('Comentario')
        else:
            # Si solo se carga la página, creamos el formulario con los datos existentes
            form = ComentarioContactoForm(instance=comentario)
    # Pasamos el formulario (ya sea vacío o con errores) a la plantilla
    return render(request, "registros/editar_comentario.html", {'form': form})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera = "TI")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(turno = "Matutino")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno', 'img')
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__contains = "Vesp")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in = ["Juan", "Ana"])
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2025, 10, 1)
    fechaFin = datetime.date(2025, 10, 25)
    alumnos = Alumnos.objects.filter(created__range = (fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar7(request):
    alumnos = Alumnos.objects.filter(comentario__coment__contains = "No inscrito")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consulta_por_fecha(request):
    fecha_inicio = datetime.date(2025, 6, 8)
    fecha_fin = datetime.date(2025, 7, 10)
    comentarios = ComentarioContacto.objects.filter(created__range=(fecha_inicio, fecha_fin))
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def consulta_por_expresion(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__contains="hola")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def consulta_por_usuario(request):
    comentarios = ComentarioContacto.objects.filter(usuario__exact="Juan")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def consulta_solo_mensajes(request):
    comentarios = ComentarioContacto.objects.values_list('mensaje')
    for mensaje in comentarios:
        print(mensaje)
    return redirect('Comentario')

def consulta_expresion_diferente(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="Es")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
    
def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html", {'alumnos':alumnos})

def seguridad(request):
    nombre = request.GET.get('nombre')
    return render(request, "registros/seguridad.html", {'nombre': nombre})