"""
entradas
valora-->A-->float
valorb-->B-->float
valorc-->C-->float

salidas
valorx1-->x1-->float
valorx2-->x2-->float
"""

#entradas
A=float(input("Ingrese el valor de a "))
B=float(input("Ingrese el valor de b "))
C=float(input("Ingrese el valor de c "))

#cajanegra
D=B**2-4*A*C

if D==0:
    x1=-B/(2*A)
    print("X1 = X2 = ",x1)  #salidas
elif D>0:
    x1=(-B+(B**2-4*A*C)**1/2)/(2*A)
    x2=(-B-(B**2-4*A*C)**1/2)/(2*A)
    print("X1= ",x1)  #salidas
    print("X2= ",x2)  #salidas
elif D<0:
    print("No tiene solucion en los reales")  #salidas