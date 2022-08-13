"""
entradas
salariobrutomensual-->sb-->float
ventasdepartamento1-->v1-->float
ventasdepartamento2-->v2-->float
ventasdepartamento3-->v3-->float

salidas
pagototaldepartamento1-->pt1-->float
pagototaldepartamento2-->pt2-->float
pagototaldepartamento3-->pt3-->float
"""

#entradas
sb=float(input("Ingrese su salario bruto mensual "))
v1=float(input("Ingrese las ventas del departamento 1 "))
v2=float(input("Ingrese las ventas del departamento 2 "))
v3=float(input("Ingrese las ventas del departamento 3 "))

#cajanegra
ig=v1+v2+v3
ex=ig*0.33

if v1>ex:
    pt1=sb*1.2
else:
    pt1=sb
if v2>ex:
    pt2=sb*1.2
else:
    pt2=sb
if v3>ex:
    pt3=sb*1.2
else:
    pt3=sb

#salidas
print("Los vendedores del deparramento 1 recibiran ",pt1)
print("Los vendedores del deparramento 2 recibiran ",pt2)
print("Los vendedores del deparramento 3 recibiran ",pt3)