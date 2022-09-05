estudiantes = { 
    "1": { 
        "nombre": "Lorea", 
        "nota": 8 
 }, 
    "2": { 
        "nombre": "Markel", 
        "nota": 4.2 
 }, 
    "3": { 
        "nombre": "Julen", 
        "nota": 6.5 
 } } 
a=3
for i in range(0,10):
    name=str(input("Nombre del estudiante: "))
    note=int(input("Nota: "))
    a=a+1
    estudiantes.update({f"{a}":{"nombre":name, "nota":note}})

suspendidos=[]
aprobados=[]
media=[]
for key in estudiantes:
    nombre=estudiantes[key]["nombre"]
    notas=estudiantes[key]["nota"]
    if notas<60:
        suspendidos.append(nombre)
    else:
        aprobados.append(nombre)
    media.append(notas)

print("Estudiantes suspendidos:",", ".join(suspendidos))
print("Estudiantes aprobados:",", ".join(aprobados))
print("La media es ",round(sum(media)/len(media),2))