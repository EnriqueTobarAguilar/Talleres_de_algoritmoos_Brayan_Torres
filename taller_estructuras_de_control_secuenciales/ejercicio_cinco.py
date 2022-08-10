#punto 5
calificacion_parcial_uno=int(input("escriba la calificacion parcial 1: "))
calificacion_parcial_dos=int(input("escriba la calificacion parcial 2: "))
calificacion_parcial_tres=int(input("escriba la calificacion parcial 3: "))
examen_final=int(input("escriba la calificacion del examen final: "))
trabajo_final=int(input("escriba la calificacion del trabajo final: "))
calificacion_final=((calificacion_parcial_uno+calificacion_parcial_dos+calificacion_parcial_tres)/3)*0.55+examen_final*0.30+trabajo_final*0.15
print ("calificacion final:",calificacion_final)