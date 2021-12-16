"""Crear una función recursiva que permita calcular el factorial de un número. 
Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial."""

def Factorial():
    try:
        num = int(input("Digite el número a calcular: "))
        x = 1
        for factor in range(1, num+1):
            x = factor * x
        print(f"El factorial de {num} es:", x)
    except Exception as e:
        print("El valor ingresado es erroneo") 
Factorial()