from django.db import models

# Create your models here.
class Gerencia(models.Model):
    nombre_gerencia= models.CharField(max_length=30)
    director= models.CharField(max_length=40)
    cant_empleados= models.IntegerField()

class Areas(models.Model):
    nombre_sector= models.CharField(max_length=30)
    cant_empleados= models.IntegerField()
    puestos_vacantes= models.IntegerField()

class Empleados(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    area= models.CharField(max_length=30)
    fecha_ingreso=models.DateField()