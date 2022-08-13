"""
entradas
numeroa-->a-->int
numerob-->b-->int
numeroc-->c-->int
numerod-->d-->int

salidas
resultado-->r-->int
"""

#entradas
a=int(input("Ingrese a "))
b=int(input("Ingrese b "))
c=int(input("Ingrese c "))
d=int(input("Ingrese d "))

#cajanegra
if d==0:
    r=(a-c)**2
elif d>0:
    r=((a-b)**3)/d

#salidas
print("El resultado es ",r)