#punto 19
cantidad_naranjas=int(input("escriba la cantidad de naranjas: "))
precio_docena=float(input("escriba el precio por docena: "))
venta=float(input("escriba la cantidad obtenida por la venta: "))
pagado=cantidad_naranjas*(precio_docena/12)
ganancia=((venta*100)/pagado)-100
print(f"el porcientaje de ganancia es: {ganancia}%")