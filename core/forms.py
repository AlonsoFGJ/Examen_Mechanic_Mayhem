from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField  # type: ignore

class EmpleadoForm(forms.ModelForm):  
    captcha = ReCaptchaField()

    class Meta:
        model = Empleado
        fields = '__all__'
        
class SubirProyectoForm(forms.ModelForm):  
    captcha = ReCaptchaField()

    class Meta:
        model = SubirProyecto
        fields = '__all__'

class GeneroForm(forms.ModelForm):  

    class Meta:
        model = Genero
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']