#punto 3
sueldo_base=float(input("escriba el sueldo base: "))
venta_uno=float(input("escriba el monto de la venta 1: "))
venta_dos=float(input("escriba el monto de la venta 2: "))
venta_tres=float(input("escriba el monto de la venta 3: "))
comisiones=(venta_uno+venta_dos+venta_tres)*0.1
sueldo_total=float(comisiones+sueldo_base)
print("Comisiones:",comisiones)
print("Sueldo Total:",sueldo_total)