from django import forms
from .models import *

class EmpleadoForm(forms.ModelForm):  

    class Meta:
        model = Empleado
        fields = '__all__'
        
class SubirProyectoForm(forms.ModelForm):  

    class Meta:
        model = SubirProyecto
        fields = '__all__'

class GeneroForm(forms.ModelForm):  

    class Meta:
        model = Genero
        fields = '__all__'