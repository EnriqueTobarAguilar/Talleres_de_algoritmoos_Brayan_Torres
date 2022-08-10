#punto 8
import math
a=float(input("escriba la medida de A "))
b=float(input("escriba la medida de B "))
c=float(input("escriba la medida de C "))
semiperimetro=(a+b+c)/2
area=math.sqrt(semiperimetro*(semiperimetro-a)*(semiperimetro-b)*(semiperimetro-c))
print("el area del triangulo es:",area)