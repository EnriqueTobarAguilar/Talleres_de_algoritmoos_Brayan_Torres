"""
entradas
combustible preferido-->f-->int

salidas
toal de cada combustible-->str
"""
a=0
d=0
g=0
while True:
    f=int(input(""))  
  #entradas
    if(f==1):
        a=a+1
    elif(f==2):
        g=g+1
    elif(f==3):
        d=d+1
    elif(f==4):
        break
print(f"MUITO OBRIGADO\nAlcool: {a} \nGasolina: {g} \nDiesel: {d}") 
#salidas