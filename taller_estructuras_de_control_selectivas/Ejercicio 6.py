"""
entradas
numeroa-->a-->int
numerob-->b-->int
numeroc-->c-->int
numerod-->d-->int
"""

#entradas
a=int(input("Ingrese a "))
b=int(input("Ingrese b "))
c=int(input("Ingrese c "))
d=int(input("Ingrese d "))


#cajanegra
if c>=5:
    n=(b+1)
    c=0
    d=0
    print(str(a)+str(n)+str(c)+str(d))  #salidas
elif c<5:
    c=0
    d=0
    print(str(a)+str(b)+str(c)+str(d))  #salidas