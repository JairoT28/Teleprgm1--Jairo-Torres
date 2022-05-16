## Numeros Impares ##

def impar():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    impares = 0
    i = 0

    while i <len(numeros):
        if numeros[i] % 2 != 0:
            impares += numeros[i]
        i += 1
    print("La suma de los numeros inpares: ", impares)

    return

impar()
