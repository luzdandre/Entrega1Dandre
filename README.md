# Entrega1Dandre
Este proyecto es una base para el desarrollo de una aplicacion para el area de RRH de una empresa

desarrolle tres modelos :
*class Gerencia = para ingresar datos del nombre de la gerencia, director y cant. de empleados
*class  Area= modelo donde se ingresa el nombre del sector, la cantidad de empleados del mismo y cuantos puestos vacantes hay
*class Empleados= trae el nombre y apellido de los empleados, el area que trabajan y fecha de intreso

Se desarrollo un formulario para cada modelo
*el formulario AreasFormulario para ingresar los datos de las Areas
*el formulario EmpleadosFormulario para ingresar los datos de los empleados
*el formulario GerenciasFormulario para ingresar la informacion de las gerencias

cada formulario se asocia a los siguientes templates:
*AreasFormulario en el template areas.html
*EmpleadosFormulario en el template empleados.html
*GerenciasFormulario en el template gerencia.html

Desarrolle un formulario de busqueda que se encuentra en el template Inicio.html , el cual permite buscar a partir del director, la gerencia correspondiente

Todos los template creados heredan el diseño del template padre.html 

se registraron los tres modelos en admin.site para poder verificar que la informacion ingresada desde la url se registra en la BD.

para eso se creo un superusuario.




