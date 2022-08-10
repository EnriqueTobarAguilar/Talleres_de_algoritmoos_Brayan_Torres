#punto 2
inversion=float(input("escriba el monto de la inversion "))
meses=int(input("escriba el tiempo en meses "))
pago=inversion*(1.02**meses)
print ("el pago sera de:",pago)