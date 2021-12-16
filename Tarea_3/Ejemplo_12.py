"""Vamos a mejorar el ejercicio anterior haciendo una función para 
validar la fecha. De tal forma que al leer una fecha se asegura que es válida."""

def DiaJuliano():
    anio = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes (numero): "))
    dia = int(input("Ingrese el dia: "))
    if (dia,mes,anio):
        c = (365.25*(anio+4716)) + (30.6001*(mes+1)) + dia + (2 - (3*anio / 400)) - 1524.5
        print(f"La fecha juliana es: {int(c)}")
    else:
        print("La fecha ingresada es erronea..")
DiaJuliano()