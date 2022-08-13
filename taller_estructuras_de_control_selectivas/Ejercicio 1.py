"""
entradas
capitalinvertido-->ci-->float
porcentajeintereses-->pi-->float

salidas
totaldedinero-->total-->float
"""

#entradas
ci=float(input("Ingrese el capital invertido "))
pi=float(input("Ingrese el porcentaje de intereses "))

#cajanegra
it=pi/100
ti=ci*it

if ti>100000:
    total=ci+(2*ti)
    print("Con el ",pi,"% de intereses, se tendra un total de ",total)  #salidas
else:
    print("Los intereses no sobrepasan los 100000 COP")  #salidas