"""
entradas
mayor-->int-->n
menor-->int-->k

salidas
numeros-->int-->n
"""
#entradas
n=int(input())
k=int(input())

#cajanegra
if k<n:
    while k<=n:
        print(n)   #salidas
        n=n-1
else:
    print("El primer numero debe ser mayor")  #salidas