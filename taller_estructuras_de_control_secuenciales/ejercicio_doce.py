#punto 12
print("Matematicas")
tarea_unom=int(input("escriba la nota tarea 1 "))
tarea_dosm=int(input("escriba la nota tarea 2 "))
tarea_tresm=int(input("escriba la nota tarea3 "))
examenm=int(input("escriba la nota examen "))
print("Fisica")
tarea_unof=int(input("escriba la nota tarea 1 "))
tarea_dosf=int(input("escriba la nota tarea 2 "))
tarea_tresf=int(input("escriba la nota tarea3 "))
examenf=int(input("escriba la nota examen "))
print("Quimica")
tarea_unoq=int(input("escriba la nota tarea 1 "))
tarea_dosq=int(input("escriba la nota tarea 2 "))
tarea_tresq=int(input("escriba la nota tarea3 "))
examenq=int(input("escriba la nota examen "))
promedio_matematicas=(examenm*0.9)+((tarea_unom+tarea_dosm+tarea_tresm)/3)*0.1
promedio_fisica=(examenf*0.8)+((tarea_unof+tarea_dosf+tarea_tresf)/3)*0.2
promedio_quimica=(examenq*0.85)+((tarea_unoq+tarea_dosq+tarea_tresq)/3)*0.15
promedio=(promedio_matematicas+promedio_fisica+promedio_quimica)/3
print("promedio de matematicas:",promedio_matematicas)
print("promedio de fisica:",promedio_fisica)
print("promedio de quimica:",promedio_quimica)
print("promedio general:",promedio)