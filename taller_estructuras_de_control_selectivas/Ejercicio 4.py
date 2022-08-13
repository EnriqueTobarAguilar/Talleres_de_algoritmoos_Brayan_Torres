"""
entradas
montodelacompra-->mc-->float

salidas
inversionempresa-->ie-->float
restante-->re-->float
restanteconintereses-->rei-->float
prestamobanco-->pb-->float
"""

#entradas
mc=float(input("Ingrese el monto de la compra "))

#cajanegra
if mc>5000000:
    ie=mc*0.55
    pb=mc*0.33
    re=mc-(ie+pb)
else:
    ie=mc*0.70
    re=mc-ie
    pb=0

rei=re*1.2

#salidas
print("La suma de ",mc, "se pagara con ",ie," por parte de los fondos de la empresa")
print(re," se pagara a credito, con el 20% de intereses para un total de ",rei)
print("El prestamo del banco sera de ",pb)