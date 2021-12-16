"""Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza 
dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro."""

def areaPerimetroCircunferencia():
    try:
        radio = float(input("Por favor digite el radio de la circunferencia: "))
        a= (radio ** 2) * 3.1415
        p= radio * 2 * 3.1415
        print(f"El area es: {round(a,4)}")
        print(f"El permitero es: {round(p,4)}")
    except Exception as e:
        print("El valor no ingresado no es valido")
areaPerimetroCircunferencia()