from django.shortcuts import render, redirect
from .models import *
from .forms  import *
from django.contrib import messages

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
            messages.success(request, "Mecánico/a creado/a correctamente")
        else:
            aux['form'] = formulario
            messages.error(request, "El Mecánico/a no se pudo crear!")

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
            messages.success(request, "Mecanico/a  modificado/a  correctamente")
        else:
            aux['form'] = formulario
            messages.error(request, "Error al modificar Mecanico/a !")

    return render(request, 'core/empleados/crud/update.html', aux)   

def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")