#punto 15
precio_pagado=float(input("escriba cual fue el precio pagado: "))
PVP=float(input("escriba el precio de venta al publico: "))
descuento=100-(precio_pagado*100)/PVP
print(f"tuvo un descuento de: {descuento}%")