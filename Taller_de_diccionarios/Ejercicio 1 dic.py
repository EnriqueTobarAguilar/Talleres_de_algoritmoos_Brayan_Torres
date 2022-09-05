lista=[12,23,5,12,92,5,12,5,29,92,64,23]
diccionario={}
for i in lista:
    contar=lista.count(i)
    diccionario.update({i:contar})
print(diccionario)    