usuarios = {
        'iperurena': {
            'nombre': 'Iñaki',
            'apellido': 'Perurena',
            'password': '123123'
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    },
        "kike": {
            "nombre": "Enrique",
            "apellido": "Tobar",
            "password": "123056" 
 }}
intentos=1
User = input("Escriba su usuario: ")
Pass = input("Escriba su password: ")
while True:
    if User in usuarios and Pass == usuarios[User]['password']:
        print(usuarios[User]["nombre"],usuarios[User]["apellido"])
        break
    else:
        print("contraseña y/o usuario incorrectos")
        User = input("Escriba su usuario: ")
        Pass = input("Escriba su password: ")
        intentos=intentos+1
    if intentos==3:
        print("Cuenta bloqueda")
        break