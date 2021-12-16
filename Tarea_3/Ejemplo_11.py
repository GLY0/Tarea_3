"""El día juliano correspondiente a una fecha es un número entero que indica los días 
que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal 
que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las
 siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano."""

def AnioBisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: 
        return False
    elif anio % 4 == 0 and anio % 100 != 0: 
        return True
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: 
        return True
AnioBisiesto(2010)

def ValidaFecha(dd,mm,aa):
    mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if AnioBisiesto(aa):
        mes[1] = 29
        
    if len(str(aa))==4:
        if mm in range(1,12):
            if (dd > 0 and dd <= mes[mm-1]):
                return True
    else:
        return False  
print(ValidaFecha(10,5,2002))

