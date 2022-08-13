"""
entradas
nombrecliente-->n-->str
montocompra-->mc-->float

salidas
montototal-->mp-->float
descuento-->d-->int
"""

#entradas
n=str(input("Ingrese su nombre "))
mc=float(input("Ingrese el monto de la compra "))

#cajanegra
if mc<500000:
    mp=mc
    d=0
elif mc>=50000 and mc<=100000:
    mp=mc*1.05
    d=5
elif mc>100000 and mc<=700000:
    mp=mc*1.11
    d=11
elif mc>700000 and mc<=1500000:
    mp=mc*1.18
    d=10
elif mc>1500000:
    mp=mc*1.25
    d=25

#salidas
print(n,", su monto de la compra es de ",mc," el monto a pagar es de ",mp," por el descuento del ",d,"%")