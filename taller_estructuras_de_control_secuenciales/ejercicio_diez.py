#punto 10
ch_austriacos=9568.71
dolar=122499
dr_griegos=886.07
fr_belgas=3237.28
fr_frances=20110
lb_esterlina=178938
li_italianas=92.89
pesetas=1
print("0. chelines austríacos")
print("1. dolar EEUU")
print("2. dracmas griego")
print("3. francos belgas")
print("4. franco francés")
print("5. libra esterlina")
print("6. liras italianas")
print("7. pesetas")
cantidad_cambiar=float(input("escriba la cantidad a cambiar: "))
moneda1=int(input("escriba el numero de la moneda a cambiar: "))
moneda2=int(input("escriba el numero de la moneda de cambio: "))
if moneda1 == 0:
  valorp=cantidad_cambiar*ch_austriacos
elif moneda1 == 1:
  valorp=cantidad_cambiar*dolar
elif moneda1 == 2:
  valorp=cantidad_cambiar*dr_griegos
elif moneda1 == 3:
  valorp=cantidad_cambiar*fr_belgas
elif moneda1 == 4:
  valorp=cantidad_cambiar*fr_frances
elif moneda1 == 5:
  valorp=cantidad_cambiar*lb_esterlina
elif moneda1 == 6:
  valorp=cantidad_cambiar*li_italianas
elif moneda1 == 7:
  valorp=cantidad_cambiar*pesetas
else :
  print("moneda a cambiar invalido")
if moneda2 == 0:
  valort=valorp/ch_austriacos
elif moneda2 == 1:
  valort=valorp/dolar
elif moneda2 == 2:
  valort=valorp/dr_griegos
elif moneda2 == 3:
  valort=valorp/fr_belgas
elif moneda2 == 4:
  valort=valorp/fr_frances
elif moneda2 == 5:
  valort=valorp/lb_esterlina
elif moneda2 == 6:
  valort=valorp/li_italianas
elif moneda2 == 7:
  valort=valorp/1
else :
  print("valor invalido")
print(f"la cantidad ${cantidad_cambiar}equivalen a ${valort} de la moneda{moneda2}")