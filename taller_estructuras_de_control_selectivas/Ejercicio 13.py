"""
entradas
mesnacimiento-->mes_nacimiento-->int
dianacimiento-->dia_nacimiento-->int
añonacimiento-->año_nacimiento-->int

salidas
edad-->años-->int
signozodiacal-->d-->str

"""
#entradas
import datetime
x=datetime.datetime.now()
mes_actual=int(x.strftime("%m"))
año_actual=int(x.strftime("%Y"))
dia_actual=int(x.strftime("%d"))

fecha_nacimiento=input("Digite en este formato: 'dd/mm/yy' : ")

day, month, year=fecha_nacimiento.split('/')
dia_nacimiento=int(day)
mes_nacimiento=int(month)
año_nacimiento=int(year)

años=0
if(dia_actual>=dia_nacimiento and mes_actual>=mes_nacimiento):
    años=año_actual-año_nacimiento
else:
    años=años=año_actual-año_nacimiento-1
print(años)


d=""
if ((mes_nacimiento==11 and dia_nacimiento>=22)or (mes_nacimiento==12 and dia_nacimiento<=21)):
    d="Sagitario"
elif ((mes_nacimiento==12 and dia_nacimiento>=22)or (mes_nacimiento==1 and dia_nacimiento<=20)):
    d="Capricornio"
elif ((mes_nacimiento==1 and dia_nacimiento>=21)or (mes_nacimiento==2 and dia_nacimiento<=19)):
    d="Acuario"
elif ((mes_nacimiento==2 and dia_nacimiento>=20)or (mes_nacimiento==3 and dia_nacimiento<=19)):
    d="Piscis"
elif ((mes_nacimiento==3 and dia_nacimiento>=21)or (mes_nacimiento==4 and dia_nacimiento<=20)):
    d="Aries"
elif ((mes_nacimiento==4 and dia_nacimiento>=21)or (mes_nacimiento==5 and dia_nacimiento<=21)):
    d="Tauro"
elif ((mes_nacimiento==5 and dia_nacimiento>=22)or (mes_nacimiento==6 and dia_nacimiento<=21)):
    d="Géminis"
elif ((mes_nacimiento==6 and dia_nacimiento>=22)or (mes_nacimiento==7 and dia_nacimiento<=22)):
    d="Cáncer"
elif ((mes_nacimiento==7 and dia_nacimiento>=23)or (mes_nacimiento==8 and dia_nacimiento<=23)):
    d="Leo"
elif ((mes_nacimiento==8 and dia_nacimiento>=24)or (mes_nacimiento==9 and dia_nacimiento<=22)):
    d="Virgo"
elif ((mes_nacimiento==9 and dia_nacimiento>=23)or (mes_nacimiento==10 and dia_nacimiento<=22)):
    d="Libra"
elif ((mes_nacimiento==10 and dia_nacimiento>=23)or (mes_nacimiento==11 and dia_nacimiento<=21)):
    d="Escorpión"
print("Usted es",d)