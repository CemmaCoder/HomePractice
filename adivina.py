import random

def adivinaElNumero(max):

    print("================================")
    print("Bienvendo, debe adivinar el n° generado al azar ")
    print("================================")
    
    aleatorio = random.randint(1,max)

    prediccion = 0
    contador = 0

    while prediccion != aleatorio:
        prediccion = int(input(f"Ingrese un numero entre 01 y {max} por favor: "))
        contador +=1
        if prediccion < aleatorio:
            print(f"El numero {prediccion} es menor al numero, intenta nuevamente")
        elif prediccion > aleatorio:
            print(f"El numero {prediccion} es mayor al numero, intenta nuevamente")
    print(f"Enhorabuena, has adivinado el numero, era el n° {aleatorio} y lo haz sacado en {contador} intentos")

adivinaElNumero(15)
