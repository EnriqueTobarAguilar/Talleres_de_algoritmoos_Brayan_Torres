"""
entradas
valor x-->x-->int
valor m-->m-->int

salidas
valor exp-->e-->int
"""
while True:
    n=input()  #entradas
    (x,m)=n.split(" ")
    x=int(x)
    m=int(m)
    if x>0 and x<=3 and m>=10 and m<=2**32-1:
        e=x*m
        print (e)  #salidas
    elif x==0 and m==0:
        break