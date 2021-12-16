"""Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

Vamos a crear las siguientes funciones para trabajar con funciones:

Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:

Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
Salir"""

def SumaFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))  
        fr01 = Fraction(n01,d01)
        fr02 = Fraction(n02,d02)
        print(f"La suma es: {fr01 + fr02}") 
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")
SumaFraccion()

def RestaFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))  
        fr01 = Fraction(n01,d01)
        fr02 = Fraction(n02,d02)
        print(f"La suma es: {fr01 - fr02}") 
    except Exception as e:
        print("valores no admitidos..")
RestaFraccion()

def MultiFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))  
        fr01 = Fraction(n01,d01)
        fr02 = Fraction(n02,d02)
        print(f"La suma es: {fr01 * fr02}") 
    except Exception as e:
        print("valores no admitidos..")
MultiFraccion()

def DivFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))  
        fr01 = Fraction(n01,d01)
        fr02 = Fraction(n02,d02)
        print(f"La suma es: {fr01 / fr02}") 
    except Exception as e:
        print("valores no admitidos..")
DivFraccion()
        