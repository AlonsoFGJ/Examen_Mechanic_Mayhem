from django.shortcuts import render, redirect
from .models import *
from .forms  import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group 


# Create your views here.
def user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def group_required(group_name):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if user_in_group(request.user, group_name):
                return view_func(request,*args, **kwargs)
            else:
                messages.error(request, 'No tienes permisos para acceder a la página')
                return redirect(to='index')
        return _wrapped_view
    return decorator

def index(request):
    return render(request, 'core/index.html')

@group_required('Cliente')
@permission_required('core.view_empleado')
def empleados(request):
    empleados = Empleado.objects.all()

    aux = {
        'lista' : empleados
    }
 
    return render(request, 'core/empleados/index.html', aux)

@permission_required('core.add_empleado')
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

@permission_required('core.change_empleado')
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

@permission_required('core.delete_empleado')
def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")

def categoriacategorias (request):
    return render(request, 'core/categorias/nuestras_categorias.html')

@group_required('Supervisor' or 'Gerente') 
def aceptar_denegar (request):
    proyectos = SubirProyecto.objects.all()
    aux2 = {
        'lista2': proyectos
    }

    return render(request, 'core/proyectos/aceptar_denegar.html', aux2)

def ultimos_trabajos (request):
    return render(request, 'core/categorias/nuestros_trabajos.html')

@group_required('Mecanico') 
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

    return render(request, 'registration/register.html', aux)
