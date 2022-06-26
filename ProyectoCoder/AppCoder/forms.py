from django import forms

class AreasFormulario(forms.Form):

    nombre_sector= forms.CharField()
    cant_empleados= forms.IntegerField()
    puestos_vacantes= forms.IntegerField()

class EmpleadosFormulario(forms.Form):

    nombre= forms.CharField()
    apellido= forms.CharField()
    area= forms.CharField()
    fecha_ingreso=forms.DateField()

class GerenciasFormulario(forms.Form):

    nombre_gerencia= forms.CharField()
    director= forms.CharField()
    cant_empleados= forms.IntegerField()