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

def categoriacategorias (request):
    return render(request, 'core/categorias/nuestras_categorias.html')

def aceptar_denegar (request):
    proyectos = SubirProyecto.objects.all()
    aux2 = {
        'lista2': proyectos
    }

    return render(request, 'core/proyectos/aceptar_denegar.html', aux2)

def ultimos_trabajos (request):
    return render(request, 'core/categorias/nuestros_trabajos.html')

def subir_proyecto(request):
    aux2 = {
        'form' : SubirProyectoForm()
    }
    
    if request.method == 'POST':
        formulario = SubirProyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Subiste un proyecto correctamente.")
        else:
            aux2['form'] = formulario
            messages.error(request, "Error al subir el proyecto.")

    return render(request, 'core/proyectos/subir_proyectos.html', aux2)

def register (request): 
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name='Cliente')
            user.groups.add(group)

            messages.success(request, "Usuario creado correctamente")
            return redirect(to="empleados")
        else: 
            aux['form'] = formulario

    return render(request, 'core/registration/register.html', aux)
