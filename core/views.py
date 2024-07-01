from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def empleados(request):
    return render(request, 'core/empleados/index.html')

def empleadosadd(request):
    return render(request, 'core/empleados/crud/add.html')    
