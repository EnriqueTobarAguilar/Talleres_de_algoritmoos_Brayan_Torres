"""
entradas
categoria-->c-->int
salariobruto-->sb-->int

salidas
c-->categoria-->int
"""

#entradas
c=int(input("Ingrese la categoria "))
sb=int(input("Ingrese el salario bruto "))

#cajanegra
if c==1:
    a=1.10
elif c==2:
    a=1.15
elif c==3:
    a=1.20
elif c==4:
    a=1.40
elif c==5:
    a=1.60

#salidas
print("De la categoria ",c, "el nuevo sueldo sera ",sb*a)