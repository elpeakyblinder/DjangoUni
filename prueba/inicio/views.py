
from django.shortcuts import render
from registros.models import Alumnos 

def principal(request):
    alumnos = Alumnos.objects.all()
    return render(request, "inicio/principal.html", {"alumnos": alumnos})

def contacto(request):
    return render(request,"inicio/contacto.html")

def formulario(request):
    return render(request, "inicio/formulario.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")