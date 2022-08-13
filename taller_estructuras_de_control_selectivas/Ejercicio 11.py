"""
entradas
temperatuta-->t-->float

salidas
deporte-->d-->str
"""

#entradas
t=float(input("Ingrese la temperatura en grados Farenheit: "))

#cajanegra
deporte=""
if(t>85 and t>120):
    deporte="Natacion"
elif(t>70 and t<=85):
    deporte="Tenis"
elif(t>32 and t<=70):
    deporte="Golf"
elif(t>10 and t<=32):
    deporte="Esqui"
elif(t>=0 and t<=10):
    deporte="Marcha"
else:
    deporte="No se encuentra en el rango"

#salidas
print("El deporte es: "+deporte)