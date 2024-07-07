from django.shortcuts import render, redirect
from .models import *
from .forms  import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def empleados(request):
    empleados = Empleado.objects.all()

    aux = {
        'lista' : empleados
    }
 
    return render(request, 'core/empleados/index.html', aux)

def empleadosadd(request):

    aux = {
        'form' : EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "Empleado/a agregado correctamente"
        else:
            aux['form'] = formulario
            aux['msj']  = "Error al agregar Empleado/a"

    return render(request, 'core/empleados/crud/add.html', aux)    

def empleadosupdate(request, id):
    empleado = Empleado.objects.get(id=id)

    aux = {
        'form' : EmpleadoForm(instance=empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = "Empleado/a modificado correctamente"
        else:
            aux['form'] = formulario
            aux['msj']  = "Error al modificado Empleado/a"

    return render(request, 'core/empleados/crud/update.html', aux)   

def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")