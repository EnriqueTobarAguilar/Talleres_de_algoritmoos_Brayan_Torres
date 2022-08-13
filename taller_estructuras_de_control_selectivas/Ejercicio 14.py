"""
entradas
lecturaanterior-->lec_an-->float
lecturaactual-->lec_ac-->float

salidas
totalapagar-->total-->float
"""

#entradas
lec_an=float(input("Ingrese la lectura anterior: "))
lec_ac=float(input("Ingrese la lectura actual: "))

#cajanegra
d=(lec_ac-lec_an)
total=""

if d>=0 and d<=100:
    total=d*4600
elif d>100 and d<=300:
    total=d*80000
elif d>300 and d<=500:
    total=d*100000
elif d>500:
    total=d*120000
else:
    print("Error en los datos")
    quit()

#salidas
print("El total a pagar es de "+str(total))