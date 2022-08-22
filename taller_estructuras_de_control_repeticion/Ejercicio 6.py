"""
entradas
dividendo-->dividendo-->int
divisor-->divisor-->int

salidas
cociente-->cociente-->int
residuo-->residuo-->int
"""
#entradas
dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))
residuo=0
cociente=0

#cajanegra
while(dividendo>=divisor):
    dividendo -=divisor
    residuo=dividendo
    cociente+=1

#salidas
print("El cociente es ",cociente)
print("El residuo es ",residuo)