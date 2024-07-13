from django.urls import path, include
from .views import *
from rest_framework import routers # type: ignore

# Configuración para el API
router = routers.DefaultRouter()
router.register('empleados', EmpleadoViewset)
router.register('generos', GeneroViewset)
router.register('tipoempleados', TipoEmpleadoViewset)

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
    path('account_locked/', account_locked, name="account_locked"),
    # REGISTER
    path('register/', register, name="register"),

    # API URLs
    path('api/', include(router.urls)),  # URLs generadas por el router de DRF
    path('empleadosapi/', empleadosapi, name="empleadosapi"),  # Ejemplo de una vista de API específica
    path('empleadodetalle/<id>/', empleadodetalle, name="empleadodetalle"),  # Vista de detalle de empleado
]
