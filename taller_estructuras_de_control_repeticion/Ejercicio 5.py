"""
salidas
numeros que pueden ser k-->k-->int
"""
k=1
sumatoria=0
while sumatoria<1000:
    sumatoria=(k**2+1)/k
    if sumatoria<1000:
        print("k puede llegar a ser ",k)  
      #salidas
    k=k+1