from django.shortcuts import render
from .models import *

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
    return render(request, 'core/empleados/crud/add.html')    

def empleadosupdate(request):
    return render(request, 'core/empleados/crud/update.html')   

def empleadosdelete(request):
    return render(request, 'core/empleados/crud/add.html')   