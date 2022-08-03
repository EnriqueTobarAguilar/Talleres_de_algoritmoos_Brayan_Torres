Algoritmo Inicio_Nombre_Apellido
	definir nombre como cadena
	definir apellido_uno como cadena
	definir apellido_dos como cadena
	definir inicial_nombre como caracter
	definir inicial_apellido_uno como caracter
	definir inicial_apellido_dos como caracter
	escribir "escriba su primer nombre: "
	leer nombre
	escribir "escriba su primer apellido: "
	leer apellido_uno 
	escribir "escriba su segundo apellido: "
	leer apellido_dos
	inicial_nombre=Subcadena(nombre,0,1)
	inicial_apellido_uno=Subcadena(apellido_uno,0,1)
	inicial_apellido_dos=Subcadena(apellido_dos,0,1)
	escribir Sin Saltar inicial_nombre
	escribir Sin Saltar inicial_apellido_uno
	escribir inicial_apellido_dos
FinAlgoritmo
