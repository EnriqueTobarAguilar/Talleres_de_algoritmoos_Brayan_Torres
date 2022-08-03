Algoritmo Inicio_Vehiculos
	escribir ' digita dos velocidades y la distancia'
	leer v1
	leer v2
	leer d
	dv =abs(v2-v1)
	th = (d/dv)
	tm = (th*60)
	escribir ' El tiempo en minutos es ' ,tm	
FinAlgoritmo
