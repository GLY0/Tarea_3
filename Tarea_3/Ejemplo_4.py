"""Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena 
con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
Crea un programa principal donde se use dicha función."""

def ConvertirEspaciado():
    cadena = input("Digite la cadena: ")
    print("Cadena Inicial: \n", cadena)
    print("Resultado de la Cadena: \n", " ".join(cadena))
ConvertirEspaciado()