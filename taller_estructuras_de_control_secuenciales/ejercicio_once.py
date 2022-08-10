#punto 11
nombre=input("escriba su nombre: ")
horas=int(input("escriba la cantidad de horas normales trabajadas: "))
precio_hora=float(input("escriba el precio de la hora trabajada: "))
horas_extra=int(input("escriba la cantidad de horas extra trabajadas: "))
hijos=int(input("escriba la cantidad de hijos: "))
salario=(horas*precio_hora)+(horas_extra*(precio_hora*1.25))
deducciones=salario*0.14
salario_neto=salario-deducciones
asignaciones=250000+(173000*hijos)+180000
print(f"{nombre}, se le asigna ${asignaciones}, se le deduce ${deducciones} y su sueldo neto es ${salario_neto}")