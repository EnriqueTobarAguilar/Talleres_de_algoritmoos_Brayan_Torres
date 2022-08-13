"""
entradas
sueldotrabajador-->s-->float

salidas
nuevosueldo-->ns-->float
"""

#entradas
s=float(input("Ingrese el sueldo "))

#cajanegra
a1=s*0.15
a2=s*0.12

if s<900000:
    ns=a1+s
else:
    ns=a2+s
    
#salidas
print("El nuevo sueldo sera ",ns)