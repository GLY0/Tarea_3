"""Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña 
y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer
 login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo."""

def Login():
    usuario = "usuario1"
    clave = "asdasd"
    intento=1
    while intento <= 3:
        usr_ = input("Digitar el usuario: ")
        pas_ = input("Digitar la clave: ")
        if (usuario == usr_ and clave == pas_):
            print("Acceso permitido")
            return
        else:
            print("acceso denegado")
            intento += 1
    if intento > 3:
        print("Ha superado el limite de intentos")
Login()