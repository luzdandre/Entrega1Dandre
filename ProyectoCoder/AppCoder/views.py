from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Gerencia, Areas, Empleados
from AppCoder.forms import AreasFormulario, EmpleadosFormulario, GerenciasFormulario
#from django.db.models import Q

# Create your views here.
def inicio(request):

    return render(request, "AppCoder/inicio.html")

def areas(request):

    return render(request, "AppCoder/areas.html")

def empleados(request):

    return render(request, "AppCoder/empleados.html")

def gerencia(request):

    return render(request,"AppCoder/gerencia.html")

def areas(request):
    if request.method == 'POST':
        miFormulario= AreasFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            areas= Areas(nombre_sector=informacion['nombre_sector'],cant_empleados=informacion['cant_empleados'],puestos_vacantes=informacion['puestos_vacantes'])

            areas.save()
            return render(request,"AppCoder/inicio.html")
    
    else:

        miFormulario= AreasFormulario()

    return render(request,"AppCoder/areas.html",{"miFormulario":miFormulario})


def empleados(request):
    if request.method == 'POST':
        miFormulario= EmpleadosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            empleados= Empleados(nombre=informacion['nombre'],apellido=informacion['apellido'],area=informacion['area'],fecha_ingreso=informacion['fecha_ingreso'])

            empleados.save()
            return render(request,"AppCoder/inicio.html")
    
    else:

        miFormulario= EmpleadosFormulario()

    return render(request,"AppCoder/empleados.html",{"miFormulario":miFormulario})  


def gerencia(request):
    if request.method == 'POST':
        miFormulario= GerenciasFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            gerencia= Gerencia(nombre_gerencia=informacion['nombre_gerencia'],director=informacion['director'],cant_empleados=informacion['cant_empleados'])

            gerencia.save()
            return render(request,"AppCoder/inicio.html")
    
    else:

        miFormulario= GerenciasFormulario()

    return render(request,"AppCoder/gerencia.html",{"miFormulario":miFormulario})



def buscar(request):
    if request.GET["director"]:
        director= request.GET['director']
        print(director)

        gerencia = Gerencia.objects.filter(director__icontains=director)
        print(gerencia)

        return render(request,"AppCoder/inicio.html", {"gerencia":gerencia,"director":director})
    
    else:
        respuesta = "No enviaste datos"

    return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})

    

