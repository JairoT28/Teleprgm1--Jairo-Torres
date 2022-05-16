## Numero mas alto ##

def numero_mas_alto():

    numero_1 = float(input("Ingrese el primer numero: "))

    numero_2 = float(input("Ingrese el segundo numero: "))

    numero_3 = float(input("Ingrese el tercer numero: "))

    if numero_1 > numero_2 and numero_1 > numero_3:
        numero__alto = numero_1
        print("El numero mas alto es: ", numero__alto)

    elif numero_2 > numero_1 and numero_2 > numero_3:
        numero__alto = numero_2
        print("El numero mas alto es: ", numero__alto)

    elif numero_3 > numero_1 and numero_3 > numero_2:
        numero__alto = numero_3
        print("El numero mas alto es: ", numero__alto)

    elif numero_1 == numero_2 and numero_1 > numero_3:
        numero__alto = numero_1
        print("El numero mas alto es: ", numero__alto)

    elif numero_1 == numero_3 and numero_1 > numero_2:
        numero__alto = numero_1
        print("El numero mas alto es: ", numero__alto)

    elif numero_2 == numero_3 and numero_2 > numero_1:
        numero__alto = numero_2
        print("El numero mas alto es: ", numero__alto)

    else:

        print("Todos los numeros son iguales")

    return()

numero_mas_alto()