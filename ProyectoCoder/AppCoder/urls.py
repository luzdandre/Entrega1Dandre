from django.urls import path

from AppCoder import views

urlpatterns= [

    path('',views.inicio,name="Inicio"),
    path('areas',views.areas,name="Areas"),
    path('empleados',views.empleados,name="Empleados"),
    path('gerencia',views.gerencia,name="Gerencia"),
    path('areasFormulario',views.areas,name="AreasFormulario"),
    path('empleadosFormulario',views.empleados,name="EmpleadosFormulario"),
    path('gerenciasFormulario',views.gerencia,name="GerenciasFormulario"),
    path('buscar/',views.buscar),
]