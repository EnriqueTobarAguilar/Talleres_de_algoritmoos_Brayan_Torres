"""
entradas
cantidadCOP-->int-->c

salidas
billetes100000-->b100-->int
billetes50000-->b50-->int
billetes20000-->b20-->int
billetes10000-->b10-->int
billetes5000-->b5-->int
billetes2000-->b2-->int
billetes1000-->b1-->int
billetes500-->b05-->int
billetes200-->b02-->int
billetes100-->b01-->int
billetes50-->b005-->int
"""

#entradas
c=int(input("Ingrese la cantidad de COP "))

#cajanegra
b100=(c-c%100000)/100000
c=c%100000
b50=(c-c%50000)/50000
c=c%50000
b20=(c-c%20000)/20000
c=c%20000
b10=(c-c%10000)/10000
c=c%10000               
b5=(c-c%5000)/5000
c=c%5000           
b2=(c-c%2000)/2000
c=c%2000                        
b1=(c-c%1000)/1000
c=c%1000                           
b05=(c-c%500)/500
c=c%500                               
b02=(c-c%200)/200
c=c%200                                   
b01=(c-c%100)/100
c=c%100                                       
b005=(c-c%50)/50

if b100>0:
    print(b100*100000)  #salida
if b50>0:
    print(b50*50000)  #salida
if b20>0:
    print(b20*20000)  #salida
if b10>0:
    print(b10*10000)  #salida
if b5>0:
    print(b5,5000)  #salida
if b2>0:
    print(b2*2000)  #salida
if b1>0:
    print(b1*1000)  #salida
if b05>0:
    print(b05*500)  #salida
if b02>0:
    print(b02*200)  #salida
if b01>0:
    print(b01*100)  #salida
if b005>0:
    print(b005*50)  #salida