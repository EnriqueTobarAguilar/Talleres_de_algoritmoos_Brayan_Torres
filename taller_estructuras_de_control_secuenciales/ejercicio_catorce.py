#punto 14
costo=float(input("escriba el costo por kw: "))
consumo=float(input("lectura de consumo anterior: "))
consumo_actual=float(input("lectura de consumo actual: "))
total=costo*(consumo_actual-consumo)
print("total a pagar:",total)