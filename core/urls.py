from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('empleados/', empleados, name="empleados"),
    path('empleados/add/', empleadosadd, name="empleadosadd"),
    path('empleados/update/<id>', empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<id>', empleadosdelete, name="empleadosdelete"),
    path('categoria/categorias/', categoriacategorias, name="categoriacategorias"),
    path('categoria/ultimos_trabajos/', ultimos_trabajos, name="ultimos_trabajos"),
    path('proyectos/subir_proyecto/', subir_proyecto, name="subir_proyecto"),
    path('proyectos/aceptar_denegar/', aceptar_denegar, name="aceptar_denegar"),

    # REGISTER
    path('register/', register, name="register"),
]
