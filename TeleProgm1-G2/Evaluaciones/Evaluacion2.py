## Creacion de tupla de 1 elemento ##S
vTupla1dato = "65737065726f2073616c6972206269656e",

## mostrar en pantalla ##
print("Mi tupla de un elemento dice:", vTupla1dato)

## print para saber que si es una tupla ##
print(type(vTupla1dato))


## Lista de edades de la poblacion que ha ido a vacunarse ##
vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]

## Eliminacion de las ocurrencias del entero 10 ##
vEdades.pop(6)
vEdades.pop(32)
vEdades.pop(39)
vEdades.pop(43)

## Ciclo for para mostrar en pantalla item por item ##
for vIndice in vEdades:
    
    print("Las edades de las personas vacunas son:", vIndice)
