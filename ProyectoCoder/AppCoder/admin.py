from django.contrib import admin

from AppCoder.models import Areas, Empleados, Gerencia

# Register your models here.

admin.site.register(Gerencia)

admin.site.register(Areas)

admin.site.register(Empleados)