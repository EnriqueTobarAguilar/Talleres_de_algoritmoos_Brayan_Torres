"""
entradas
edadenmeses-->m-->int
sexo-->s-->str
nivelhemoglobina-->h-->float

salidas
negativo-->n-->str
positivo-->n-->str
"""

#entradas
m=int(input("Ingrese su edad en meses "))
s=str(input("Ingrese su sexo (M para mujer o H para hombre)) "))
h=float(input("Ingrese su porcentaje de hemoglobina "))

#cajanegra
n=("Negativo para anemia")
p=("Positivo para anemia")

if m>=0 and m<=1:
    if h>=13 and h<=26:
        print(n)  #salidas
    elif h<13:
        print(p)  #salidas
elif m>1 and m<=6:
    if h>=10 and h<=18:
        print(n)  #salidas
    elif h<10:
        print(p)  #salidas
elif m>6 and m<=12:
    if h>=11 and h<=15:
        print(n)  #salidas
    elif h<11:
        print(p)  #salidas
elif m>12 and m<=60:
    if h>=11.5 and h<=15:
        print(n)  
    elif h<11.5:
        print(p)  #salidas
elif m>60 and m<=120:
    if h>=12.6 and h<=15.5:
        print(n)  #salidas
    elif h<12.6:
        print(p)  #salidas
elif m>120 and m<=180:
    if h>=13 and h<=15.5:
        print(n)  #salidas
    elif h<13:
        print(p)  #salidas
elif m>180:
    if s=="M" or s=="m":
        if h>=12 and h<=16:
            print(n)  #salidas
        elif h<12:
            print(p)  #salidas
    elif s=="H" or s=="h":
        if h>=14 and h<=18:
            print(n)  #salidas
        elif h<12:
            print("Positivo para anemia")  #salidas
else:
    print("Error en los datos")    #salidas