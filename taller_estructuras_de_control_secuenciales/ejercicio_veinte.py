#punto 20
precio_contado=float(input("escriba cual es el precio de contado: "))
precio_credito=float(input("escriba el precio a credito por cuota: "))
intereses=((precio_credito*100)/(precio_contado/12))-100
print(f"se le cobra {intereses}% de intereses por cuota")