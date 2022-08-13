"""
entradas
distanciarecorrida-->km-->float

salidas
valortotalapagar-->nd-->float
"""

#entradas
d=float(input("Ingrese los km recorridos "))

#cajanegra
if d<=300:
    print("El valor a pagar es de 50000 COP")  #salidas
elif d>300 and d<=1000:
    nd=((d-300)*30000)+70000
    print("El valor a pagar es de ",nd," COP")  #salidas
elif d>1000:
    nd=((d-1000)*9000)+150000
    print("El valor a pagar es de ",nd," COP")  #salidas