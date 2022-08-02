Algoritmo Inicio_vendedor
	escribir 'cuanto es su sueldo'
	leer sueldo
	escribir 'venta uno'
	leer venta_uno
	escribir 'venta dos'
	leer venta_dos
	escribir 'venta tres'
	leer venta_tres
	comisiones=(venta_uno+venta_dos+venta_tres)*0.1
	sueldo_total=sueldo+comisiones
	escribir sin saltar 'total de comisiones es: '
	escribir comisiones
	escribir sin saltar 'total de sueldo es: '
	escribir sueldo_total
FinAlgoritmo