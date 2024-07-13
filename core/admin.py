from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin # type: ignore
from django.contrib.admin import ModelAdmin
from django.contrib.auth.forms import AuthenticationForm
from django_recaptcha.fields import ReCaptchaField  # type: ignore

class GeneroModelAdmin(AdminConfirmMixin, admin.ModelAdmin):
        confirm_change = True
        confirmation_fields = ['descripcion']

class TipoEmpleadoModelAdmin(AdminConfirmMixin, admin.ModelAdmin):
        confirm_change = True
        confirmation_fields = ['descripcion']

class EmpleadoModelAdmin(AdminConfirmMixin, admin.ModelAdmin):
        confirm_change = True
        confirmation_fields = ['rut', 'nombre', 'apellido', 'edad', 'direccion', 'telefono']

class CategoriasModelAdmin(AdminConfirmMixin, admin.ModelAdmin):
        confirm_change = True
        confirmation_fields = ['descripcion']

class SubirProyectoModelAdmin(AdminConfirmMixin, admin.ModelAdmin):
        confirm_change = True
        confirmation_fields = ['titulo', 'nombre_mecanico', 'categoria','valor','descripcion','nombre_cliente']

class ProductosModelAdmin(AdminConfirmMixin, admin.ModelAdmin):
        confirm_change = True
        confirmation_fields = ['titulo', 'descripcion', 'precio']

class CustomAdminLoginForm(AuthenticationForm):
    captcha = ReCaptchaField()

admin.site.login_form = CustomAdminLoginForm

# Register your models here.
admin.site.register(Genero,GeneroModelAdmin)
admin.site.register(TipoEmpleado,TipoEmpleadoModelAdmin)
admin.site.register(Empleado,EmpleadoModelAdmin)
admin.site.register(Categorias,CategoriasModelAdmin)
admin.site.register(SubirProyecto,SubirProyectoModelAdmin)
admin.site.register(Productos,ProductosModelAdmin)