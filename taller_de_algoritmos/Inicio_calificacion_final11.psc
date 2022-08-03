Algoritmo Inicio_calificacion_final
	escribir 'calificacion primer parcial'
	leer primer_parcial
	escribir 'calificacion segundo parcial'
	leer segundo_parcial
	escribir 'calificacion tercer parcial'
	leer tercer_parcial
	escribir 'calificacion examen final'
	leer examen_final
	escribir 'calificacion trabajo final'
	leer trabajo_final
	calificacion_final=((primer_parcial+segundo_parcial+tercer_parcial)/3)*0.55+examen_final*0.30+trabajo_final*0.15
	escribir sin saltar 'calificacion final es: '
	escribir calificacion_final
FinAlgoritmo
